# Rclone

`rclone` is a command line tool to sync files and directories to and from all major cloud storage sites. You can use `rclone` to sync files and directories between Yale clusters and Yale Box, google drive, etc. The following instructions cover basics to setup and use `rclone` on Yale clusters. For more information about Rclone, please visit its website at [https://rclone.org](https://rclone.org). 

## Set up Rclone on YCRC clusters

Before accessing a remote cloud storage using `rclone`, you need to run `rclone config` to configure 
the storage for `rclone`. Since `rclone config` will try to bring up a browser for you to authorize 
the cloud storage, we recommend you to use [Open OnDemand](https://docs.ycrc.yale.edu/clusters-at-yale/access/ood/). 

To run `rclone config` on OOD, first click `Remote Desktop` from the OOD dashboard. 
Once a session starts running, click `Connect to Remote Desktop` and 
you will see a terminal on the desktop in the browser. 
Run `rclone config` at the command line of the terminal. 

![ood_dashboard](/img/rclone-ood-dashboard.png){: .medium}

![ood_remote](/img/rclone-remote-desktop.png){: .medium}

During configuration, you will see a message similar to the following: 
```
If your browser does not open automatically go to the following link: http://127.0.0.1:53682/auth
Log in and authorize rclone for access
Waiting for code...
```
If no browser started automatically, then start Firefox manually by clicking 
the Firefox icon on the top bar of the Remote Desktop. 
Copy the link from the message shown on your screen and paste it to the address bar of Firefox.
Log in with your Yale email address, respond to the DUO request, and authorize the access. 

!!! Tip
    If you received an error stating that your session has expired for DUO, simply paste the link and reload the page.  If you still get the expired message, log out of CAS in your browser by going to https://secure.its.yale.edu/cas/logout.  After logging out, paste the link and reload.

## Examples

The following examples show you how to set up rclone for Google Drive and Yale Box.
In both examples, we name our remote cloud storage as 'remote' in the configuration. 
You can provide any name you want. 

--8<-- "snippets/rclone_examples.md"

!!! Tip
    if you want to use rclone for a shared google drive, you should answer 'y' when it asks whether you want to configure it as a Shared Drive.

    ```bash
    Configure this as a Shared Drive (Team Drive)?
    y) Yes
    n) No (default)
    y/n> y
    ```

!!! Tip
    `rclone config` creates a file storing cloud storage configurations for rclone. 
    You can check the file name with `rclone config file`. The config file can be 
    copied to other clusters so that you can use `rclone` on the other clusters without running `rclone config` again.

## Use Rclone on Yale clusters

As we have used `remote` as the name of the cloud storage in our examples above, 
we will continue using it in the following examples. 
You should replace it with the actual name you have picked up for the cloud storage in your configuration. 

!!! Tip
    If you forgot the name of the cloud storage you have configured, run `rclone config show` and the name will be shown in `[]`. 
    ```bash
    $ rclone config show
    [remote]
    type = drive
    scope = drive
    token = {"access_token":"mytoken","expiry":"2021-07-09T22:13:56.452750648-04:00"}
    root_folder_id = myid
    ```

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
