# Transfer Data

Transferring files can be done using several methods. The most common are described below.

## Data Transfer Nodes

Each cluster (except for Milgram) has a dedicated "data transfer" node that is specially networked for high speed transfers both on and off-campus using the Yale Science Network. These transfer nodes are also the hosts of our [Globus service](#large-transfers-globus), which enables resilient transfers of large amounts of data. From the login node of a cluster, you can ssh to the transfer node:

```
ssh transfer
```

If you are initiating a longer running transfer and are not using [Globus](#large-transfers-globus), you can initiate the transfer in a [tmux](/clusters-at-yale/guides/tmux/) session to protect against network interruptions.

You may also use the transfer node to transfer data from your local machine using one of the below methods. From off-cluster, the nodes are accessible at the following hostnames. Note that you still must be on-campus or the [VPN](/clusters-at-yale/access/vpn/) to access the transfer nodes.

| Cluster   | Transfer Node                          |
|-----------|----------------------------------------|
| Grace     | `transfer-grace.hpc.yale.edu`          |
| Farnam    | `transfer-farnam.hpc.yale.edu`         |
| Ruddle    | `transfer-ruddle.hpc.yale.edu`         |
| Milgram   | use login node: `milgram.hpc.yale.edu` |

## scp/rsync (macOS/Linux only)

Linux and Apple macOS users can use [scp](https://linux.die.net/man/1/scp) or [rsync](http://linux.die.net/man/1/rsync) to transfer files to/from a cluster. You will need the hostname of the cluster transfer node (see above) to transfer files.

Note that you must have your ssh keys properly setup to use the commands outlined below. See the [Cluster Access documentation](/clusters-at-yale/access) for more info.

scp and sftp are both used from a Terminal window. The basic syntax of `scp` is

```
scp [from] [to]
```

The “from” portion can be a filename or a directory/folder. The “to” portion will contain your netid, the hostname of the cluster transfer node (or login node for Milgram), and the destination directory/folder.

### Transfer a File from Your Computer to a Cluster

Assuming the user’s netid is `ra359`, the following is run on your computer's local terminal.

```
scp myfile.txt ra359@transfer-grace.hpc.yale.edu:/home/fas/admins/ra359/test
```

In this example, `myfile.txt` is copied to the directory `/home/fas/admins/ra359/test:` on Grace. This example assumes that `myfile.txt` is in your current directory. You may also specify the full path of `myfile.txt`.

```
scp /home/xyz/myfile.txt ra359@transfer-grace.hpc.yale.edu:/home/fas/admins/ra359/test
```

### Transfer a Directory to a Cluster

```
scp -r mydirectory ra359@transfer-grace.hpc.yale.edu:/home/fas/admins/ra359/test
```

In this example, the contents of `mydirectory` are transferred. The `-r` indicates that the copy is recursive.

### Transfer Files from the Cluster to Your Computer

Assuming you would like the files copied to your current directory:

```
scp ra359@transfer-grace.hpc.yale.edu:/home/fas/admins/ra359/myfile.txt .
```

Note that `.` represents your current working directory.
To specify the destination, simply replace the `.` with the full path:

```
scp ra359@transfer-grace.hpc.yale.edu:/home/fas/admins/ra359/myfile.txt /path/myfolder
```

## FTP Client

You can also transfer files between your local computer and a cluster using an FTP client, such as [Cyberduck (OSX/Windows)](https://cyberduck.io/) or [FileZilla (Linux)](https://filezilla-project.org/). You will need to configure the client with your netid as the username, the cluster transfer node as the hostname and your private key as the authentication method. An example configuration of Cyberduck is shown below.

![Cyberduck sample configuration.](/img/cyberduck.png)

### FTP on Ruddle

If you are connecting to  Ruddle, which requires [Multi-Factor Authentication](/clusters-at-yale/access/mfa), there are a couple additional steps.

You will need to change the Cyberduck preferences to "Use browser connection" instead of "open multiple connections". This can be found under `Cyberduck > Preferences > Transfers > General`.

Then once you establish your connection, you will prompted with a "Partial authentication success" window. In the password field, type in "push" to receive a push approval notification to the Duo app on your phone. Alternate multi-factor authentications can be used by enter the following words in the password field:

* "push" to receive a push notification to your smart phone (requires the Duo mobile app)
* "sms" to receive a verification passcode via text message
* "phone" to receive a phone call

## Object Storage Transfers

To move data to and from object stores such as AWS S3, or GCP cloud storage, we recommend using rclone. It is installed as a module on all of the clusters.  You can use to to copy files, sync directories, etc.  See <http://rclone.org>

To begin, configure a connection by running

```bash
rclone configure
```

You'll be prompted for a name for the connection (e.g mys3), and then details about the connection.  Once you've saved that configuration, you can use that connection name to copy files:

```bash
rclone copy localpath/myfile mys3:bucketname/
rclone sync localpath/mydir mys3:bucketname/remotedir
```

We recommend that you protect your configurations with a password.  You'll see that as an option when you run rclone config.

## Large Transfers (Globus)

For larger transfers both within Yale and to external collaborators, we recommend using Globus. Globus is a file transfer service that is efficient and easy to use. It has several advantages:

* Globus can robustly and quickly transfer large files, and large collections of files
* Files can be transferred between your computer and the clusters
* Files can be transferred between Yale and other sites
* There is a simple web interface for starting and monitoring transfers, as well as a command line interface.
* You can provide access to specific files or directories to non-Yale people in a secure way.

We have set up Globus endpoints on most of the Yale clusters. Globus uses gridftp to perform transfers in parallel. Globus works a bit differently than other transfer services such as ftp or rsync. With Globus, files are always transferred between two "endpoints". One endpoint is always a Globus server, such as the ones we've set up on the clusters. The other endpoint can be a second server, or a Globus connect personal endpoint, which is a desktop application.

### Get Started with Globus (using Farnam as an example)

1. In a browser, go to www.globus.org.
1. Click on "Login".
1. Use the pulldown to select Yale in the list of organizations and click "Continue".
1. If you are not already logged into CAS, you will be asked for netid and password.
    1. If you have never logged in before: do not associate with another account unless you are familiar with doing this
    1. If you have never logged in before: select 'non-profit research or educational purposes'
    1. If you have never logged in before: click on 'Allow' for allowing Globus Web App
1. In the column on the left side, click on the 'ENDPOINTS' icon (a circle circled by another circle)
1. Use the text bar to search for yale#farnam
1. Click on 'yale#farnam' "Managed Public Endpoint" to get to the File Manager Overview tab
1. Click on 'Open in File Manager' (option is on the right-hand side of the screen)
1. You'll see a transfer panel with dual panes with your Farnam data on the left. Enter an endpoint name in the right endpoint box (eg: your personal endpoint)
1. Select one or more files in either the left or right box, and click the < or > button to transfer the files in that direction.

### Sharing Data Using Globus (using Farnam as an example)

1. Follow the instructions above until you have the Farnam endpoint opened in the file manager
1. Click on the icon that shows a folder with two shoulder-to-head silhouettes in front of it
1. Click on 'Add a Shared Endpoint'
1. Click on 'Browse' to find and select the path you want to share
1. Add other details as desired and click on 'Create Share'
1. Click on 'Add Permissions -- Share With'
1. Under 'Username or Email' enter the e-mail address of the person that you want to share the data with, then click on 'Save', then click on 'Add Permission'
1. Do not select 'write' unless you want the person you are sharing the data with to be able to write to the share. 


For more information, please see the [official Globus Documentation](https://docs.globus.org).

### Cluster Endpoints

We currently support endpoints for the following clusters.

| Cluster   | Globus Endpoint       |
|-----------|-----------------------|
| Grace     | `yale#grace`          |
| Farnam    | `yale#farnam`         |
| Ruddle    | `yale#ruddle`         |

All of these endpoints provide access to all files you normally have access to, except sequencing data on Ruddle.

### Google Drive Endpoints

See our [Google Drive Documentation](/data/google-drive) for instructions for using Globus to transfer data to Eliapps Google Drive.

### Setup an Endpoint on Your Own Computer

You can set up your own endpoint for transferring data to and from your own computer. This is called Globus Connect, and you can find instructions [here](https://www.globus.org/globus-connect).

## Share Data with non-Yale Collaborators

Among Globus' greatest features is the ability to allow collaborators at other institutions access to specific files or directories. This is done by creating a "shared endpoint" and setting the permissions on that endpoint. Please the [official Globus documentation](https://docs.globus.org/how-to/share-files/) on sharing for detailed instructions.

