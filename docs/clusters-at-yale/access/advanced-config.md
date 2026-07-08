# Advanced SSH Configuration

## Example SSH `config`

The following configuration is an example ssh client configuration file specific to our clusters. You can use it on Linux, [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10), and macOS. It allows you to use tab completion of the clusters, without the `.ycrc.yale.edu` suffixes (i.e. `ssh bouchet` or `scp ~/my_file bouchet:my_file` should work). It will also allow you to re-use and multiplex authenticated sessions. This means although the clusters require [Duo MFA](/clusters-at-yale/access/mfa), it will not force you to re-authenticate, as you use the same ssh connection to host multiple sessions. If you attempt to close your first connection with others running, it will wait until all others are closed.

Save the text below to `~/.ssh/config` and replace `NETID` with your Yale netid. Lines that begin with `#` will be ignored.

```

# If you use a ssh key that is named something other than id_rsa,
# you can specify your private key like this:
# IdentityFile ~/.ssh/other_key_rsa

# Uncomment the ForwardX11 options line to enable X11 Forwarding by default (no -Y necessary)
# On a Mac you still need xquartz installed

Host *.ycrc.yale.edu bouchet grace mccleary milgram misha
    User NETID
    #ForwardX11 yes
    # To re-use your connections with multi-factor authentication
    # Uncomment the two lines below
    #ControlMaster auto
    #ControlPath /tmp/%h_%p_%r
    #ControlPersist 2h

Host bouchet grace mccleary milgram misha
    HostName %h.ycrc.yale.edu
```

For more info on ssh configuration, run:

``` bash
man ssh_config
```

## Store Passphrase and Use SSH Agent on macOS

By default, macOS won't always remember your ssh key passphrase and keep your ssh key in the agent for SSH agent forwarding. In order to not repeatedly enter your passphrase and instead store it in your keychain, enter the following command on your Mac (just once):


``` bash

# In MacOS version 12.0 Monterey or newer
ssh-add --apple-use-keychain ~/.ssh/id_rsa

# Older MacOS version
ssh-add -K ~/.ssh/id_rsa
```

Or whatever your private key file is named.

!!! note
    If you use homebrew your default OpenSSH may have changed. To add your key(s) to the system ssh agent, use the absolute path: `/usr/bin/ssh-add`

Then and add the following to your `~/.ssh/config` file (create this file if it doesn't exist, or add these settings to the `Host *.ycrc.yale.edu ...` rule if it does).

```
Host *.ycrc.yale.edu mccleary grace milgram misha
    UseKeychain yes
    AddKeystoAgent yes
```

You can view a list of the keys currently in your agent with:

``` bash
ssh-add -L
```

## SSH Agent on Windows

In a PowerShell terminal:
```powershell
# By default the ssh-agent service is disabled. Configure it to start automatically.
# Make sure you're running as an Administrator.
Get-Service ssh-agent | Set-Service -StartupType Automatic

# Start the service
Start-Service ssh-agent

# This should return a status of Running
Get-Service ssh-agent

# Now load your key files into ssh-agent
ssh-add $env:USERPROFILE\.ssh\<your_keyfile>
```

## SSH tunneling for local applications

Note: These instructions work with recent versions of macOS. You may have to adjust them to work with other operating systems.

SSH tunneling can allow local applications to connect to YCRC clusters. Connecting to the cluster requires two-factor authentication. Some applications, such as [VSCode](/clusters-at-yale/access/ood-vscode) or [Jupyter Notebooks](clusters-at-yale/guides/jupyter_ssh), can handle this form of authentication, but others, such as Claude Science, do not currently support it. For programs like these, you can establish the tunnel separately in the terminal and perform authentication there. Then, you can point the application to the authenticated tunnel. This is a general approach that also works with VSCode or Notebooks.

There are many different ways to set up a local tunnel using SSH. The approach outlined below has two main parts

1. A one-time SSH configuration step.
2. A few simple commands to allocate a compute node and connect to it.

First, add these two host blocks to `~/.ssh/config`, replacing YOUR_NETID and PATH_TO_YOUR_SSH_KEY. You only need to perform this step once

These instructions assume you are on bouchet but can be adjusted for other clusters. The first block, `bouchet-tunnel` will be used when you establish the tunnel. Once you have the tunnel running, you will point your application to `bouchet-compute`, which will then use the tunnel to connect to the cluster.

```bash
# Used to establish a tunnel to a bouchet compute node
Host bouchet-tunnel
   HostName bouchet.ycrc.yale.edu
   User YOUR_NETID
   SessionType none
   ExitOnForwardFailure yes
   ServerAliveInterval 30
   ServerAliveCountMax 4
   IdentityFile PATH_TO_YOUR_SSH_KEY
   IdentitiesOnly yes

# Used to connect a local application to the tunnel
Host bouchet-compute
   HostName localhost
   Port 2222
   User YOUR_NET_ID
   UserKnownHostsFile ~/.ssh/known_hosts_bouchet-compute
   StrictHostKeyChecking accept-new
   IdentityFile PATH_TO_YOUR_SSH_KEY
   IdentitiesOnly yes
```

Second, request a compute node and start a tunnel to it. You'll have to run these commands every time you request a new compute node.

On Bouchet, allocate a compute node
```bash
salloc
hostname -s #e.g, a1130u05n01
```

Open a local terminal on your laptop and start the local tunnel. Use the host name from your allocated compute node from the previous step. This example uses `a1130u05n01`, but you should update the command to reflect the host name of your allocated compute node.

```bash
ssh -L 2222:a1130u05n01:22 bouchet-tunnel
```

Within the terminal, you will be asked to authenticate using two-factor authentication. After authenticating, SSH prints "Success. Logging you in...", and then pauses. Keep the terminal open; closing it will close the tunnel.

Your tunnel is now open! Refer to application specific instructions to connect your application to `bouchet-compute`
