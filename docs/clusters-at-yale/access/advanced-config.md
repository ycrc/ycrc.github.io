# Advanced SSH Configuration

## Example SSH `config`

The following configuration is an example ssh client configuration file specific to our clusters. You can use it on Linux, [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10), and macOS. It allows you to use tab completion of the clusters, without the `.ycrc.yale.edu` suffixes (i.e. `ssh grace` or `scp ~/my_file grace:my_file` should work). It will also allow you to re-use and multiplex authenticated sessions. This means although the clusters require [Duo MFA](/clusters-at-yale/access/mfa), it will not force you to re-authenticate, as you use the same ssh connection to host multiple sessions. If you attempt to close your first connection with others running, it will wait until all others are closed.

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
