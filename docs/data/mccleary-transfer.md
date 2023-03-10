# Transfer data from Farnam/Ruddle to McCleary

In the process of migrating from Farnam and Ruddle to McCleary, we are requesting researchers migrate their own data.
Researchers are encouraged to only transfer data which is actively needed and take this opportunity to archive or delete old data. 
Transfers should be initiated on Farnam or Ruddle's `transfer` nodes and sync'd to either Gibbs project directories (`/gpfs/gibbs/project/GROUP/NETID`) or their McCleary home spaces (which are mounted at `/vast/palmer/home.mccleary/NETID`).
All users are able to log into the `transfer` nodes via ssh:

```sh
[tl397@farnam1 ~]$ ssh transfer
[tl397@transfer-farnam ~]$
```

!!! Warning 
	Do not attempt to transfer conda environments to McCleary. 
	Environments are not portable and will not work properly if simply copied.
	Instead, please export and rebuild environments following our [guide](/clusters-at-yale/guides/conda-export).

The two tools we recommend for this transfer are `rsync` and `Globus`.
`rsync` is a command-line utility which copies files, along with their attributes, with protections against file corruption. 
`Globus` is a web app where you can schedule large transfers which occur in the background and provide notifications when complete.
Since McCleary mounts Farnam and Ruddle's filesystems, these copies are "local" copies and should run at high speed.
`rsync` is best suited for smaller data transfers, while `Globus` is our recommended tool for larger transfers. 

In this short note we will detail these two approaches.


## Rsync 

While `rsync` is most commonly used for remote transfers between two systems, it is an excellent tool for local work as well.
In particular, it's ability to perform tests to make sure that files are transfered properly and to recover from interrupted transfers make it a good option for data migration.
There are many configuration possibilities, but we recommend using the following flags:

```sh
rsync -avP /path/to/existing/data /path/to/new/home/for/data
```

Here the `-a` will run the transfer in `archive` mode, which preserves ownership, permissions, and creation/modification times.
Additionally, the `-v` will run in `verbose` mode where the name of every file is printed out, and `-P` displays a progress bar.

One subtle detail is that `rsync` changes its behavior based on whether the source path has a trailing `/`. 
If one initiates a sync like this:
```sh
rsync -avP /path/to/existing/data /path/to/new/home/for/data
```
the existing `data` directory is transferred as a whole entity, including the top-level directory `data`.
However, if the source path includes a trailing `/`:

```sh
rsync -avP /path/to/existing/data/ /path/to/new/home/for/data
```
then the contents of data are transferred, omitting the top-level directory. 

As an example, to transfer a directory (named `my_data`) from a YSM project directory to your Gibbs project space, you can run:

```sh
rsync -avP /gpfs/ysm/project/GROUP/NETID/my_data /gpfs/gibbs/project/GROUP/NETID/
```

Similarly, to transfer a directory (`my_code`) from your YCGA homespace to your new McCleary homespace:

```sh
rsync -avP /home/NETID/my_code /vast/palmer/home.mccleary/NETID/
```

where `GROUP` and `NETID` are replaced by your specific group/netid.

For more detailed information about `rsync`, please take a look at this nice tutorial ([link](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories)).

For `rsync` transfers that may take a while, it's best to run the transfer inside a [tmux](https://github.com/tmux/tmux/wiki/Getting-Started) virtual login session.
This enables you to "detach" from the session while the transfer continues in the background.
`tmux` uses special key-strokes to control the session, with the most important being `Ctrl-b d` (first pressing the `control` and `b` keys, releasing, and then pressing `d`) which detaches from the current session.
To reattach to a detached session, run `tmux attach` from the same host where `tmux` was initially started.
For more information about `tmux`, please see their [Getting Started Guide](https://github.com/tmux/tmux/wiki/Getting-Started).


## Globus

Yale provides dedicated Globus connections for each of the clusters following the naming convention `yale#cluster_name`. 
Transfers can be managed through existing accounts on Farnam or Ruddle, using `yale#farnam` or `yale#ruddle`.
For a general getting started with Globus, please check out their [website](https://docs.globus.org/how-to/get-started/).
We have a stand-alone docs page about Globus [here](/data/globus), but here we will detail the process to transfer data from YSM (for example) to the Gibbs file system.

1. log in to [app.globus.org](https://app.globus.org) and use your Yale credentials to authenticate. 
2. navigate to the File Manager and access Farnam or Ruddle by searching for the "collection" `yale#farnam` or `yale#ruddle` in the left-hand panel.
3. find the files you wish to transfer, using the check-boxes to select any and all files needed.
4. click on the "Transfer or Sync to" option and in the right-hand panel also search for the same cluster's (either `yale#farnam` or `yale#ruddle`) collection.
5. navigate through the file-browser to find the desired destination for these data (most likely `gibbs_project` or a subdirectory).
6. start the transfer, click the "Start" button on the left-hand side.

This will start a background process to transfer all the selected files and directories to their destination.
You will receive an email when the transfer completes detailing the size and average speed of the transferred data.

## Getting help

If you run into any issues or if you would like help in setting up your data migration, please feel free to reach out to hpc@yale.edu to request one-on-one support.
