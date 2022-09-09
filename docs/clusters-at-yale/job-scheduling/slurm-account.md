# Slurm Account Coordinator

On the clusters the YCRC maintains, we map your linux user and group to your Slurm user and account, which is what actually gives you permission to submit to the various partitions available on the clusters. By changing the Slurm accounts associated with your user, you can modify access to partitions. As a coordinator of an account, you have permission to modify users' association with that account and modify jobs running that are associated with that account. Below are some useful example commands where we use an example user with the name "be59" where you are the coordinator of the slurm account "cryoem".

## Add/Remove Users From an Account

``` bash
sacctmgr add user be59 account=cryoem # add user
sacctmgr remove user where user=be59 and account=cryoem # remove user
```

## Show Account Info

``` bash
sacctmgr show assoc user=be59 # show user associations
sacctmgr show assoc account=cryoem # show assocations for account
```

## Submit Jobs

``` bash
salloc -A cryoem ...
sbatch -A cryoem my_script.sh
```

## List Jobs

``` bash
squeue -A cryoem  # by account
squeue -u be59 # by user
```

## Cancel Jobs

``` bash
scancel 1234  # by job ID
scancel -u be59   # kill all jobs by user
scancel -u be59 --state=running  # kill running jobs by user
scancel -u be59 --state=pending  # kill pending jobs by user
scancel -A cryoem  # kill all jobs in the account
```

## Hold and Release Jobs
```
scontrol hold 1234   # by job ID
scontrol release 1234   # remove the hold
scontrol uhold 1234   # hold job 1234 but allow the job's owner to release it
```