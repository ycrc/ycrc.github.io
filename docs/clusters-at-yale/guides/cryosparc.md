# cryoSPARCv2 on Farnam

Getting cryoSPARC set up and running on the YCRC clusters is something of a task. This guide is meant for intermediate/advanced users. If enought people can convince Structura bio ([see ticket here](https://discuss.cryosparc.com/t/external-authentication-methods/2736)) to make cryoSPARC more cluster-friendly we could have a single instance running that you'd just log in to with your Yale credentials. Until then, venture below at your own peril.

## Install

Before you get started, you will need to request a licence from Structura [from their website](https://cryosparc.com/download/). These instructions are gently modified from the [official cryoSPARC documentation](https://cryosparc.com/docs/reference/install/). 

### 1. Set up Environment

First allocate an interactive job on a compute node to run the install on. 

``` bash
salloc --cpus-per-task 2
```

Then, set the following environment variables to suit your install. We filled in some defaults for you.

``` bash
# where to install cryosparc2 and its sample database
install_path=$( readlink -f ${HOME}/project )/software/cryosparc2

# the license ID you got from Structura
license_id=

# your email
my_email=$(head -n1 ~/.forward)

# slurm partition to submit your cryosparc jobs to
# not sure you can change at runtime?
partition=gpu
```

### 2. Set up Directories, Download installers

``` bash
# your username
my_name=${USER}
# a temp password
cryosparc_passwd=Password123

# load the right CUDA
module load CUDA/9.0.176

# set up some more paths
db_path=${install_path}/database
worker_path=${install_path}/cryosparc2_worker
ssd_path=/tmp/${USER}/cryosparc2_cache

# go get the installers
mkdir -p $install_path
cd $install_path
curl -sL https://get.cryosparc.com/download/master-latest/$license_id > cryosparc2_master.tar.gz
curl -sL https://get.cryosparc.com/download/worker-latest/$license_id > cryosparc2_worker.tar.gz

tar -xf cryosparc2_master.tar.gz
tar -xf cryosparc2_worker.tar.gz
```

### 3. Install the Server and Worker

``` bash
cd ${install_path}/cryosparc2_master
./install.sh --license $license_id --hostname $(hostname) --dbpath $db_path --yes
source ~/.bashrc

cd ${install_path}/cryosparc2_worker
./install.sh --license $license_id --cudapath $CUDA_HOME --yes
source ~/.bashrc
```

### 4. Configure for Farnam
``` bash
# Farnam cluster setup
mkdir -p ${install_path}/site_configs && cd ${install_path}/site_configs
cat << EOF > cluster_info.json
{
    "name" : "farnam",
    "worker_bin_path" : "${install_path}/cryosparc2_worker/bin/cryosparcw",
    "cache_path" : "/tmp/{{ cryosparc_username }}/cryosparc_cache",
    "send_cmd_tpl" : "{{ command }}",
    "qsub_cmd_tpl" : "sbatch {{ script_path_abs }}",
    "qstat_cmd_tpl" : "squeue -j {{ cluster_job_id }}",
    "qdel_cmd_tpl" : "scancel {{ cluster_job_id }}",
    "qinfo_cmd_tpl" : "sinfo"
}
EOF

cat << EOF > cluster_script.sh
#!/usr/bin/env bash
#SBATCH --job-name cryosparc_{{ project_uid }}_{{ job_uid }}
#SBATCH -c {{ num_cpu }}
#SBATCH --gpus={{ num_gpu }}
#SBATCH -p ${partition}
#SBATCH --mem={{ (ram_gb*1024)|int }}
#SBATCH -o {{ job_dir_abs }}
#SBATCH -e {{ job_dir_abs }}

module load CUDA/9.0.176
mkdir -p /tmp/${USER}/cryosparc2_cache
{{ run_cmd }}
EOF
```

## Run

``` bash
salloc --cpus-per-task 2
master_host=$(hostname)
base_dir=$(dirname "$(dirname "$(which cryosparcm)")")
sed -i.bak 's/export CRYOSPARC_MASTER_HOSTNAME.*$/export CRYOSPARC_MASTER_HOSTNAME=\"'"$master_host"'\"/g' $base_dir/config.sh
source $base_dir/config.sh
cryosparcm start
cryosparcm status

# run the output from the following command on your local linux/mac machine
echo "ssh -N -L $CRYOSPARC_BASE_PORT:$master_host:$CRYOSPARC_BASE_PORT $USER@mccleary.ycrc.yale.edu"
```

## Database errors

If your database won't start and *_you're sure_* there isn't another server running, you can remove lock files and try again.

``` bash
# rm -f $CRYOSPARC_DB_PATH/WiredTiger.lock $CRYOSPARC_DB_PATH/mongod.lock
```