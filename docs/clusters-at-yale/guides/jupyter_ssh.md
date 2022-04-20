# Jupyter Notebooks over SSH Port Forwarding

If you want finer control over your notebook job, or wish to use something besides `conda` for your Python environment, you can manually configure a Jupyter notebook and connect manually.

The main steps are:

1. Start a Jupyter notebook job.
1. Start an ssh tunnel.
1. Use your local browser to connect.

### Start the Server

Here is a template for submitting a jupyter-notebook server as a batch job. 
You may need to edit some of the slurm options, including the time limit or the partition. 
You will also need to either load a module that contains `jupyter-notebook`.

!!! tip
    If you are using a Conda environment, please follow the instructions for launching a Jupyter session via [Open OnDemand](/clusters-at-yale/ood).

Save your edited version of this script on the cluster, and submit it with `sbatch`.

``` bash
#!/bin/bash
#SBATCH --partition interactive
#SBATCH --cpus-per-task 1
#SBATCH --mem-per-cpu 8G
#SBATCH --time 6:00:00
#SBATCH --job-name jupyter-notebook
#SBATCH --output jupyter-notebook-%J.log
#SBATCH --chdir $HOME

# get tunneling info
XDG_RUNTIME_DIR=""
port=$(shuf -i8000-9999 -n1)
node=$(hostname -s)
user=$(whoami)
cluster=$(hostname -f | awk -F"." '{print $2}')

# print tunneling instructions jupyter-log
echo -e "
For more info and how to connect from windows,
   see https://docs.ycrc.yale.edu/clusters-at-yale/guides/jupyter/
MacOS or linux terminal command to create your ssh tunnel
ssh -N -L ${port}:${node}:${port} ${user}@${cluster}.hpc.yale.edu
Windows MobaXterm info
Forwarded port:same as remote port
Remote server: ${node}
Remote port: ${port}
SSH server: ${cluster}.hpc.yale.edu
SSH login: $user
SSH port: 22
Use a Browser on your local machine to go to:
localhost:${port}  (prefix w/ https:// if using password)
"

# load modules or conda environments here

jupyter-notebook --no-browser --port=${port} --ip=${node}
```

### Start the Tunnel

Once you have submitted your job and it starts, your notebook server will be ready for you to connect. 
You can run `squeue -u${USER}` to check. You will see an "R" in the ST or status column for your notebook job if it is running. 
If you see a "PD" in the status column, you will have to wait for your job to start running to connect. 
The log file with information about how to connect will be in the directory you submitted the script from, and be named jupyter-notebook-[jobid].log where jobid is the slurm id for your job.

#### MacOS and Linux

On a Mac or Linux machine, you can start the tunnel with an SSH command. 
You can check the output from the job you started to get the specifc info you need.

#### Windows

On a Windows machine, we recommend you use MobaXterm. 
See our guide on [connecting with MobaXterm](/clusters-at-yale/access) for instructions on how to get set up. 
You will need to take a look at your job's log file to get the details you need. 
Then start MobaXterm:

1. Under Tools choose "MobaSSHTunnel (port forwarding)".
1. Click the "New SSH Tunnel" button.
1. Click the radio button for "Local port forwarding".
1. Use the information in your jupyter notebook log file to fill out the boxes.
1. Click Save.
1. On your new tunnel, click the key symbol under the settings column and choose your ssh private key.
1. Click the play button under the Start/Stop column.

## Browse the Notebook

Finally, open a web browser on your local machine and enter the address `http://localhost:port` where port is the one specified in your log file. 
The address Jupyter creates by default (the one with the name of a compute node) will not work outside the cluster's network. 
Since version 5 of jupyter, the notebook will automatically generate a token that allows you to authenticate when you connect. 
It is long, and will be at the end of the url jupyter generates. 
It will look something like

`http://c14n06:9230/?token=**ad0775eaff315e6f1d98b13ef10b919bc6b9ef7d0605cc20**`

If you run into trouble or need help, [contact us](/#get-help).
