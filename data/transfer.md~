# Transfer Data

For all transfer methods, you need to have [set up your 
account](/clusters-at-yale/access) on the cluster(s) you want to transfer data to/from.

## Data Transfer Nodes

Each cluster has dedicated nodes specially networked for high speed transfers both on and off-campus using the Yale Science Network. 
You may use transfer nodes to transfer data from your local machine using one of the below methods. 
From off-cluster, the nodes are accessible at the following hostnames. 
You must still be on-campus or on the [VPN](/clusters-at-yale/access/vpn/) to access the transfer nodes.

| Cluster   | Transfer Node                          |
|-----------|----------------------------------------|
| Bouchet   | `transfer-bouchet.ycrc.yale.edu`       |
| Grace     | `transfer-grace.ycrc.yale.edu`         |
| McCleary  | `transfer-mccleary.ycrc.yale.edu`      |
| Milgram   | `transfer-milgram.ycrc.yale.edu`       |
| Misha     | `transfer-misha.ycrc.yale.edu`         |


From the login node of any cluster, you can `ssh` into the transfer node. 
This is useful for transferring data to or from locations other than your local machine (see below for details).

```
[netID@cluster ~] ssh transfer
```

## Transferring Data to/from Your Computer

### Graphical Transfer Tools

#### Web Transfers with Open OnDemand

On each cluster, you can use their respective [Open OnDemand](/clusters-at-yale/access/ood/#File-Browser) portals to transfer files.
This works best for small numbers of relatively small files. You can also directly edit scripts through this interface, alleviating the need to transfer scripts to your computer to edit.

### File Transfers with Globus

You can use the Globus service to perform data transfers between your local machine and the clusters.
Globus provides a robust and resumable way to transfer larger files or datasets as well as an easy to use interface for tranfers between your local machine and the clusters.
Please see [our Globus page](/data/globus) for Yale-specific documentation and [their official docs](https://docs.globus.org/how-to) to get started.

### Command-Line Transfer Tools

#### scp and rsync (macOS/Linux/Linux on Windows)

Linux and macOS users can use [scp](https://linux.die.net/man/1/scp) or [rsync](http://linux.die.net/man/1/rsync). Use the hostname of the cluster transfer node (see above) to transfer files. These transfers must be initiated from your local machine.

scp and sftp are both used from a Terminal window. The basic syntax of `scp` is

``` bash
scp [from] [to]
```

The from and to can each be a filename or a directory/folder on the computer you are typing the command on or a remote host (e.g. the transfer node).

#### Example: Transfer a File from Your Computer to a Cluster

Using the example netid `abc123`, following is run on your computer's local terminal.

``` bash
scp myfile.txt abc123@transfer-grace.ycrc.yale.edu:/home/abc123/test/
```

In this example, `myfile.txt` is copied to the directory `/home/abc123/test/` on Grace. This example assumes that `myfile.txt` is in your current directory. You may also specify the full path of `myfile.txt`.

``` bash
scp /home/xyz/myfile.txt abc123@transfer-grace.ycrc.yale.edu:/home/abc123/test/
```

#### Example: Transfer a Directory to a Cluster

``` bash
scp -r mydirectory abc123@transfer-grace.ycrc.yale.edu:/home/abc123/test/
```

In this example, the contents of `mydirectory` are transferred. The `-r` indicates that the copy is recursive.

#### Example: Transfer Files from the Cluster to Your Computer

Assuming you would like the files copied to your current directory:

``` bash
scp abc123@transfer-grace.ycrc.yale.edu:/home/abc123/test/myfile.txt .
```

Note that `.` represents your current working directory.
To specify the destination, simply replace the `.` with the full path:

``` bash
scp abc123@transfer-grace.ycrc.yale.edu:/home/abc123/test/myfile.txt /path/myfolder
```

## Transfer Data Between Clusters

### Globus Endpoints

Globus is a web-enabled GridFTP service that transfers large datasets fast, securely, and reliably between computers configured to be endpoints. 
Please see [our Globus page](/data/globus) for Yale-specific documentation and [their official docs](https://docs.globus.org/how-to) to get started.

* We have configured endpoints for most of the Yale clusters and many other institutions and compute facilities have Globus endpoints. 
* You can also use Globus to transfer data to/from Eliapps Google Drive and S3 buckets.

### Cluster Transfer Nodes

You can transfer data between clusters using the transfer nodes.
Connecting from one cluster to another is made simple and smooth by using [`ssh-agent`](https://en.wikipedia.org/wiki/Ssh-agent) to forward your ssh keys. 
This avoids the need to explicitly add each cluster's ssh key to the list of Authorized Keys. 

!!! Tip
    If you are running a large transfer without [Globus](/data/globus), run it inside a [tmux](/clusters-at-yale/guides/tmux/) session on the transfer node. This protects your transfer from network interruptions between your computer and the transfer node.


```bash
# add ssh keys to ssh-agent
[user@local ~]$ ssh-add

# ssh to cluster with forwarded agent 
[user@local ~]$ ssh -A netID@mccleary.ycrc.yale.edu

# connect to the transfer node from the login node
[netID@mccleary ~]$ ssh -A transfer

# copy data to cluster storage
[netID@transfer1-mccleary ~]$ rsync -avP $HOME/path/to/data netID@transfer-bouchet.ycrc.yale.edu:~/
```

The rsync connection will use the forwarded key and you will not need to reauthenticate. 

## Transfer Data to Outside of Yale

If the location you are transfering to supports Globus, that is the preferred tool for transferring large data off-site.
Please see [our Globus page](/data/globus) for more details.

For data that is primarily hosted elsewhere and is only needed on the cluster temporarily, see our guide on [Staging Data](/data/staging) for additional information. 
For any data that hosted outside of Yale, you will need to initiate the transfer from the cluster's data transfer node as the clusters are not accessible without the VPN. 

### rsync

```bash
# connect to the transfer node from the login node
[netID@bouchet ~] ssh transfer

# pull data from remote to cluster
[netID@transfer1-bouchet ~]$ rsync -avP user_name@remote_host:/path/to/data ./

# push data from cluster to remote
[netID@transfer1-bouchet ~]$ rsync -avP ~/path/to/data user_name@remote_host:/path/to/data 

```

### Rclone

To move data to and from cloud storage (Box, Dropbox, Wasabi, AWS S3, or Google Cloud Storage, etc.), we recommend using [Rclone](/clusters-at-yale/guides/rclone.md). It is installed on all of the clusters and can be installed on your computer.

### Sites Behind a VPN

If you need to transfer data to or from an external site that is only accessible via VPN, please [contact us](/#get-help) for assistance as we might be able to provide a workaround to enable a direct transfer between the YCRC clusters and your external site.
