# cryoSPARC on McCleary

Getting cryoSPARC set up and running on the YCRC clusters is something of a task. This guide is meant for intermediate/advanced users. YCRC staff are working on a cryoSPARC application for [Open OnDemand](/clusters-at-yale/access/ood.md) Until then, venture below at your own peril.

## Install

Before you get started, you will need to request a licence from Structura [from their website](https://cryosparc.com/download/). These instructions are gently modified from the [official cryoSPARC documentation](https://cryosparc.com/docs/reference/install/). 

### 1. Set up Environment

First, get an interactive session or an Open Ondemand Remote Desktop in a partition with GPUs that you have access to.  Remember to request a non-zero number of GPUs.

Then choose a location for installing the software, such as under your project directory.

``` bash
export install_path=${HOME}/project/cryosparc
mkdir -p ${install_path}
```

### 2. Set up Directories, Download installers

``` bash
export LICENSE_ID=Your-cryosparc-license-code-here

 #go get the installers
cd $install_path
curl -L https://get.cryosparc.com/download/master-latest/$LICENSE_ID -o cryosparc_master.tar.gz
curl -L https://get.cryosparc.com/download/worker-latest/$LICENSE_ID -o cryosparc_worker.tar.gz

tar -xf cryosparc_master.tar.gz
tar -xf cryosparc_worker.tar.gz
```

### 3. Install the Standalone Server/Worker

``` bash

# Load a cluster CUDA module
 
cd ${install_path}/cryosparc_master
module load CUDA/11.8.0
export cuda_path=${EBROOTCUDA}

# Set a temporary password
export cryosparc_passwd=Password123

export db_path=${install_path}/cryosparc_database
export worker_path=${install_path}/cryosparc_worker
export ssd_path=/tmp/${USER}
mkdir $ssd_path
export user_email="Your email address"

# Run the installation script
cd ${install_path}/cryosparc_master

./install.sh --standalone \
--license $LICENSE_ID \
--worker_path $worker_path \
--ssdpath $ssd_path \
--initial_email $user_email \
--initial_password $cryosparc_passwd \
--initial_username ${USER} \
--initial_firstname "Firstname" \
--initial_lastname "Lastname"
```

!!!warning
     If you are installing a version of cryoSPARC older than 4.4.0, add the additional line

     ``` bash
     --cudapath $cuda_path \
     ```

     after the --ssdpath line.

``` bash

# Set location of cryoSPARC executables
source ~/.bashrc
```

## Run

### 1. Launch cryoSPARC server

The installation process will normally attempt to launch cryoSPARC automatically.  Check its status and launch manually if need be.

``` bash
cryosparcm status
cryosparcm start (if not running) 
```

### 2. Access the cryoSPARC interface

In your interactive session with –x11, or Open OnDemand Remote Desktop, launch a browser and go to https://localhost:39000 . Log in with your email and the password you chose above.

### 3. Clean up

When you are finished with your current cryoSPARC session,

``` bash
cryosparcm stop
```

and shut down your Open OnDemand session.

### 4. Relaunch

You are not guaranteed to get the same GPU node every time, so you need to set cryoSPARC to use whichever one you are running on.  Once you have started a new GPU node session,

``` bash
mkdir /tmp/${USER}
export master_host=$(hostname)
export base_dir=$(dirname "$(dirname "$(which cryosparcm)")")

sed -i.bak 's/export CRYOSPARC_MASTER_HOSTNAME.*$/export CRYOSPARC_MASTER_HOSTNAME=\"'"$master_host"'\"/g' $base_dir/config.sh

source $base_dir/config.sh

cryosparcm start
```

and then connect to https://localhost:39000 as above.

### 5. Running on multiple nodes

In principle, you can request multiple nodes for your job session, and configure cryoSPARC to use additional nodes as worker nodes. Contact YCRC staff for assistance.
  
## Troubleshoot

If you are unable to start a new cryoSPARC instance, the likeliest reason is leftover files from a previous run that was not shut down properly. Check /tmp and /tmp/${USER} for the existence of a cryosparc*.sock file or a mongo*.sock file.  If they are owned by you, you can just remove them, and cryoSPARC should start normally.  If they are not owned by you, and you have reserved the GPUs, then it is likely due to another user's interrupted job.  Contact YCRC staff for assistance.


If your database won't start and *_you're sure_* there isn't another server running, you can remove lock files and try again.

``` bash
# rm -f $CRYOSPARC_DB_PATH/WiredTiger.lock $CRYOSPARC_DB_PATH/mongod.lock
```
