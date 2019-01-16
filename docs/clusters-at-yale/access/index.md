# Log on to the Clusters

We use `ssh` with ssh key pairs to log in to the clusters, e.g.

```
ssh netid@clustername.hpc.yale.edu
```

If you have a public key and are familiar with key pairs, upload your ssh key below. Please allow up to fifteen minutes for the key to propogate before logging in.

*   [Upload your SSH key here](http://gold.hpc.yale.internal/cgi-bin/sshkeys.py) (only accessible on campus or through the Yale VPN)
*   [Troubleshoot Login](/clusters-at-yale/troubleshoot)

For additional information, see below.

*   [Off Campus Access to the Clusters](vpn)
*   Graphical Interfaces: [X11 Forwarding](x11) and [VNC](vnc)

## Connect from macOS and Linux

### Generate Your Key Pair

A key pair is required to connect to a cluster. A key pair consists of a private key and a public key. The private key remains on your desktop/laptop and should never be shared with anyone. Your public key is installed in `~/.ssh/authorized_keys` on the cluster. In order for someone to access your account on the cluster, they must possess your private key and its associated passphrase.

To generate a new key pair, first open a terminal/xterm session. If you are on macOS, open Applications -> Utilities -> Terminal.

Generate your public and private ssh keys. Type the following into the terminal window:

```
ssh-keygen
```

Your terminal should respond:

```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/#yourusername#/.ssh/id_rsa):

```

Press Enter to accept the default value. Your terminal should respond:

```
Enter passphrase (empty for no passphrase):
```

Choose a secure passphrase. Your passphrase will prevent access to your account in the event your private key is stolen. The response will be:

```
Enter same passphrase again:
```

Enter the passphrase again. The key pair is generated and written to a directory called `.ssh` in your home directory. The public key is stored in `~/.ssh/id_rsa.pub`. If you forget your passphrase, it cannot be recovered. Instead, you will need to generate and upload a new ssh key pair.

Next, install your public ssh key on the cluster. Run the following command in a terminal:

```
cat ~/.ssh/id_rsa.pub
```

Copy and paste the output to [Yale HPC ssh key installer](http://gold.hpc.yale.internal/cgi-bin/sshkeys.py) (only accessible on campus or through the Yale VPN). It may take up to 15 minutes after uploading for your key to be pushed to the clusters. Note that you should never send the private key file to anyone!

### Connect

Once your public key has been installed, you may use ssh in a terminal to access the appropriate cluster. You need to know 2 things to log into a cluster.

1.  The hostname of the cluster login node
2.  Your netid

You can find the hostnames of the cluster login nodes [here.](/clusters-at-yale/clusters) Open a terminal window and connect to the login node using the syntax:

```
ssh netid@login-node
```

For example, if your netid is `ra359` and you wish to log into the Grace cluster:

```
ssh ra359@grace.hpc.yale.edu
```

Check out our [Sample Linux/Mac SSH Configuration](sample-config) for tips on maintaining connections and adding tab complete to your ssh commands.


### Mac: Store Passphrase and Use SSH Agent Forwarding

By default, macOS won't always remember your ssh key passphase and keep your ssh key in the agent for SSH agent forwarding. In order to not repeatedly enter your passphrase and enable agent forwarding, enter the following command on your local machine (just once):

```
ssh-add -K ~/.ssh/[your-private-key]

```

and add the following to your `~/.ssh/config` file (create this file if it doesn't exist).

```
Host *
    UseKeychain yes
    AddKeystoAgent yes
    ForwardAgent yes
```

## Connect from Windows

We recommend using [MobaXterm](https://mobaxterm.mobatek.net/) to connect to the clusters. You can download, extract & install MobaXterm from [this page](https://mobaxterm.mobatek.net/download-home-edition.html). We recommend using the "Installer Edition", but make sure to extract the zip file before running the installer.

### Generate Your Key Pair

To get up and running, generate an ssh keypair if you haven't already:

*   From the top menu choose Tools -> MobaKeyGen (SSH key generator).
*   Leave all defaults and click the generate button.
*   Wiggle your mouse.
*   Save your public key as id_rsa.pub.
*   Save your private key as id_rsa.ppk (this one is secret, don't give it to other people).
*   Copy the text of your public key and paste it into the text box after you log into [the SSH key uploader](http://gold.hpc.yale.internal/cgi-bin/sshkeys.py).
*   Your key will be synced out to the clusters in a few minutes.

### Connect

To make a new connection to one of the clusters

*   From the top menu select Sessions -> New Session.
*   Click the SSH icon in the top left.
*   Enter the cluster login node address (e.g. farnam.hpc.yale.edu) as the Remote Host.
*   Check "Specify Username" and Enter your netID as the the username.
*   Click the "Advanced SSH Settings" tab and check the "Use private key box", then click the file icon / magnifying glass to choose where you saved your private key (id_rsa.ppk).
*   Click OK.

![Sample SSH Configuration](/img/ssh_connection.png)

In the future, your session should be saved in the sessions bar on the left in the main window.