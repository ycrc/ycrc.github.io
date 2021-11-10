# Transfer Data

For all transfer methods, you need to have [set up your account](/clusters-at-yale/access) on the cluster(s) you want to tranfer data to/from.

## Data Transfer Nodes

Each cluster (except Milgram) has dedicated nodes specially networked for high speed transfers both on and off-campus using the Yale Science Network. You may use transfer nodes to transfer data from your local machine using one of the below methods. From off-cluster, the nodes are accessible at the following hostnames. You must still be on-campus or on the [VPN](/clusters-at-yale/access/vpn/) to access the transfer nodes.

| Cluster   | Transfer Node                          |
|-----------|----------------------------------------|
| Grace     | `transfer-grace.hpc.yale.edu`          |
| Farnam    | `transfer-farnam.hpc.yale.edu`         |
| Ruddle    | `transfer-ruddle.hpc.yale.edu`         |
| Milgram   | use login node, `milgram.hpc.yale.edu` |

From the login node of any cluster (except Milgram), you can `ssh` into the transfer node. This is useful for transferring data to locations other than your local machine (see below for details).

```
[netID@cluster ~] ssh transfer
```


## Transferring Data to/from Your Local Machine

### Graphical Transfer Tools

#### OOD Web Transfers

On each cluster, you can use their respective [Open OnDemand](/clusters-at-yale/access/ood/#File-Browser) portals to transfer files. This works best for small numbers of relatively small files. You can also directly edit scripts through this interface, alleviating the need to transfer scripts to your computer to edit.

#### MobaXterm (Windows)

[MobaXterm](/clusters-at-yale/access/#windows) is an all-in-one graphical client for Windows that includes a transfer pane for each cluster you connect to. Once you have established a connection to the cluster, click on the "Sftp" tab in the left sidebar to see your files on the cluster. You can drag-and-drop data into and out of the SFTP pane to upload and download, respectively.

#### Cyberduck

You can also transfer files between your local computer and a cluster using an FTP client, such as [Cyberduck (OSX/Windows)](https://cyberduck.io/). You will need to configure the client with your netid as the username, the cluster transfer node as the hostname and your private key as the authentication method. An example configuration of Cyberduck is shown below.

![Cyberduck sample configuration.](/img/cyberduck.png)

##### Cyberduck on Ruddle

Ruddle requires [Multi-Factor Authentication](/clusters-at-yale/access/mfa) so there are a couple additional configuration steps. Under `Cyberduck > Preferences > Transfers > General` change the setting to "Use browser connection" instead of "Open multiple connections".

When you connect type one of the following when prompted with a "Partial authentication success" window.

* "push" to receive a push notification to your smart phone (requires the Duo mobile app)
* "sms" to receive a verification passcode via text message
* "phone" to receive a phone call

### Large File Transfers (Globus)

You can use the Globus service to perform larger data transfers between your local machine and the clusters. Globus provides a robust and resumable way to transfer larger files or datasets. Please see [our Globus page](/clusters-at-yale/data/globus) for Yale-specific documentation and [their official docs](https://docs.globus.org/how-to) to get started.

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
scp myfile.txt abc123@transfer-grace.hpc.yale.edu:/home/fas/admins/abc123/test
```

In this example, `myfile.txt` is copied to the directory `/home/fas/admins/abc123/test:` on Grace. This example assumes that `myfile.txt` is in your current directory. You may also specify the full path of `myfile.txt`.

``` bash
scp /home/xyz/myfile.txt abc123@transfer-grace.hpc.yale.edu:/home/fas/admins/abc123/test
```

#### Example: Transfer a Directory to a Cluster

``` bash
scp -r mydirectory abc123@transfer-grace.hpc.yale.edu:/home/fas/admins/abc123/test
```

In this example, the contents of `mydirectory` are transferred. The `-r` indicates that the copy is recursive.

#### Example: Transfer Files from the Cluster to Your Computer

Assuming you would like the files copied to your current directory:

``` bash
scp abc123@transfer-grace.hpc.yale.edu:/home/fas/admins/abc123/myfile.txt .
```

Note that `.` represents your current working directory.
To specify the destination, simply replace the `.` with the full path:

``` bash
scp abc123@transfer-grace.hpc.yale.edu:/home/fas/admins/abc123/myfile.txt /path/myfolder
```

## Transfer Data to/from Other Locations 

### Globus Endpoints

Globus is a web-enabled GridFTP service that transfers large datasets fast, securely, and reliably between computers configured to be endpoints. Please see [our Globus page](/clusters-at-yale/data/globus) for Yale-specific documentation and [their official docs](https://docs.globus.org/how-to) to get started.

*  We have configured endpoints for most of the Yale clusters and many other institutions and compute facilities have Globus endpoints. 
* You can also use Globus to transfer data to/from Eliapps Google Drive and S3 buckets.

### Cluster Transfer Nodes

You can use the cluster transfer nodes to download/upload data to locations off-cluster. For data that is primarily hosted elsewhere and is only needed on the cluster temporarily, see our guide on [Staging Data](/clusters-at-yale/data/staging) for additional information. For any data that hosted outside of Yale, you will need to initiate the transfer from the cluster's data transfer node as the clusters are not accessible without the VPN. On Milgram, which does not have a transfer node, you can initiate the transfers from a login node. However, please be mindful of that other users will also be using the login nodes for regular cluster operations.

!!! Tip
    If you are running a large transfer without [Globus](/clusters-at-yale/data/globus), run it inside a [tmux](/clusters-at-yale/guides/tmux/) session on the transfer node. This protects your transfer from network interruptions between your computer and the transfer node.

#### rsync

```
# connect to the transfer node from the login node
[netID@cluster ~] ssh transfer
# copy data to cluster storage
[netID@transfer ~]$ rsync -avP netID@department_server:/path/to/data $HOME/scratch60/
```

#### Rclone

To move data to and from cloud storage (Box, Dropbox, Wasabi, AWS S3, or Google Cloud Storage, etc.), we recommend using [Rclone](https://rclone.org/). It is installed as a module on all of the clusters and can be installed on your computer. You will need to configure it for each kind of storage you would like to transfer to with:

```bash
module load rclone
rclone configure
```

You'll be prompted for a name for the connection (e.g mys3), and then details about the connection.  Once you've saved that configuration, you can connect to the transfer node (using `ssh transfer` from the login node) and then use that connection name to copy files with similar syntax to `scp` and `rsync`:

```bash
rclone copy localpath/myfile mys3:bucketname/
rclone sync localpath/mydir mys3:bucketname/remotedir
```

We recommend that you protect your configurations with a password. You'll see that as an option when you run rclone config. For all the Rclone documentaion please [refer to the official site](https://rclone.org/docs/).
