# Rclone

`rclone` is a command line program to sync files and directories to and from all major cloud storage sites and services. You can use `rclone` to sync files and directories between Yale clusters and Yale Box, google drive, etc. The following instructions covers basics to setup and use `rclone` on Yale clusters. For more information about Rclone, please visit its website at [https://rclone.org](https://rclone.org). 

## Setup Rclone on Yale clusters

You need to run `rclone config` at least once to receive authorization for access to the cloud service which you are configuring. Since `rclone config` will bring up a browser to authorize the cloud service, you will need X Windows on the host where you run `rclone config`. This means, to setup `rclone` on one of the Yale clusters, you need to login to the cluster with [X11 forwarding](https://docs.ycrc.yale.edu/clusters-at-yale/access/x11/). However X11 forwarding is extremly slow and you may have problems of brining up the browser smoothly. A better way is to run VNC on the cluster and setup a tunnel to access the [remote VNC desktop](https://docs.ycrc.yale.edu/clusters-at-yale/access/vnc/) on the cluster. A third way, which is the best, is to use the Remote Desktop App from the [OnDemand portal](https://docs.ycrc.yale.edu/clusters-at-yale/access/ood/). Once Remote Desktop starts runing, do the following in the terminal:

The example below is a screen dump from setting up `rclone` on Farnam for Yale Box.
```
[pl543@transfer-farnam ~]$ rclone config
2019/10/21 09:14:05 NOTICE: Config file "/home/pl543/.config/rclone/rclone.conf" not found - using defaults
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n
name> remote
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
[snip]
 6 / Box
   \ "box"
[snip]
Storage> box
** See help for box backend at: https://rclone.org/box/ **

Box App Client Id.
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_id> 
Box App Client Secret
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_secret> 
Edit advanced config? (y/n)
y) Yes
n) No
y/n> n
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes
n) No
y/n> y
If your browser does not open automatically go to the following link: http://127.0.0.1:53682/auth
Log in and authorize rclone for access
Waiting for code...
(In the browser opened, login with your Yale email and password. You will be redirect to CAS authentication. This may take a while.)
Got code
--------------------
[remote]
type = box
token = {"access_token":"PjIXHUZ34VQSmeUZ9r6bhc9ux44KMU0e","token_type":"bearer","refresh_token":"VumWPWP5Nd0M2C1GyfgfJL51zUeWPPVLc6VC6lBQduEPsQ9a6ibSor2dvHmyZ6B8","expiry":"2019-10-21T11:00:36.839586736-04:00"}
--------------------
y) Yes this is OK
e) Edit this remote
d) Delete this remote
y/e/d> y
Current remotes:

Name                 Type
====                 ====
remote               box

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q
```

`rclone setup` creates a file that stores all the config of `rclone`. You can check the file name with `rclone config file`. The config file can be copied to other clusters so that you can use `rclone` on the other clusters without running `rclone config` again.

Setting up `rclone` for "Google Drive" follows a similar procedure. 

## Use Rclone on Yale clusters

### List files

```
rclone ls remote:/
```

### Copy files 
```
rclone copy remote:/path/to/filename .
rclone copy filename remote:/path/to/
```

### Help
```
rclone help
```
