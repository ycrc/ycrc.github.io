# Clean Out Omega Data

All Omega files are now stored solely on the Loomis GPFS system. Omega data can be accessed from Grace and Farnam for copying and clean-up until February 1, 2019\. **If you have data on Omega that you would like to keep, you will need to move it to a new location before February 1, 2019, after which it will be permanently deleted.**

Omega data can be accessed from the other clusters at the following paths until that date:

```
/gpfs/loomis/home.omega/<metagroup>/<group>/<netid>
/gpfs/loomis/scratch.omega/<metagroup>/<group>/<netid>
```

You can run the `mydirectories` command from the clusters for the proper paths of your directories. Note that Omega logins have been disable for most users, so you will need follow the instructions below to access your data. **Those users who still have access to Omega, your scratch space will become read-and-delete-only on Monday, December 3, 2018\. To continue to compute, please redirect your job output to your Grace project or scratch60 spaces.** Gaussian users, see below for tips on redirecting Gaussian's output.

If you are a PI and would like access to data owned by any former group members, please send us an email at [hpc@yale.edu](mailto:hpc@yale.edu) and we can assist you.

## Review Usage

From either Grace or Farnam, you can run the groupquota script with the `-c omega` flag to get a report of your group's storage usage on Omega.

```
getquota -c omega
```

If you don't have an account on Grace or Farnam, you can email us at [hpc@yale.edu](mailto:hpc@yale.edu) to get a list of usage and see below for instructions on retrieving your data.

## Transferring Data from Omega to Grace or Farnam

Since the Loomis is available on Grace and Farnam, there is no need to use Globus or rsync that data between transfer nodes. Instead, from the cluster where you will be storing the data moving forward, you can run an `rsync` directly between the filesets (directory trees). Once you have copied your data from Omega to your other cluster, **please delete the data from the Omega directories**. For example, if you would like to copy your data into a new directory in your project space:

```
>mkdir ~/project/data_from_omega
rsync -avz /gpfs/loomis/scratch.omega/fas/hpcprog/kln26/simulation100 ~/project/data_from_omega
# verify data has been copied successfully to ~/project/data_from_omega, then
rm -r /gpfs/loomis/scratch.omega/fas/hpcprog/kln26/simulation100
```

Again, please delete any data you have copied off the Omega storage spaces or determined you no longer need.

## Transferring Data from Omega off of Cluster Storage

If you had an account on Omega but don't use either of Grace or Farnam, you can use Globus to transfer data from the `yale#omega` endpoint.

Please see our [data transfer documentation](/cluster-at-yale/data/transfer)  for instructions on transferring to local storage.

Please see our [Google Drive documentation](/data/google-drive) for instructions on transferring to Google Drive.

Again, please delete any data you have copied off the Omega storage spaces or determined you no longer need, which you should be able to do from the Globus interface.