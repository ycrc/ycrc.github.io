# Advanced SSH Configuration

## Example SSH `config`

The following configuration is an example ssh client configuration file specific to our clusters. You can use it on Linux, [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10), and macOS. It allows you to use tab completion of the clusters, without the `.hpc.yale.edu` suffixes (i.e. `ssh grace` or `scp ~/my_file grace:my_file` should work). It will also allow you to re-use and multiplex authenticated sessions. This means clusters that require [Duo MFA](/clusters-at-yale/access/mfa) will not force you to re-authenticate, as you use the same ssh connection to host multiple sessions. If you attempt to close your first connection with others running, it will wait until all others are closed.

Save the text below to `~/.ssh/config` and replace `NETID` with your Yale netid. Lines that begin with `#` will be ignored.

```

# If you use a ssh key that is named something other than id_rsa,
# you can specify your private key like this:
# IdentityFile ~/.ssh/other_key_rsa

# Uncomment the ForwardX11 options line to enable X11 Forwarding by default (no -Y necessary)
# On a Mac you still need xquartz installed
Host *.hpc.yale.edu grace milgram ruddle
    User NETID
    #ForwardX11 yes
    # To re-use your connections with multi-factor authentication
    # Uncomment the two lines below
    #ControlMaster auto
    #ControlPath ~/.ssh/tmp/%h_%p_%r

Host *.ycrc.yale.edu mccleary
    User NETID
    #ForwardX11 yes
    # To re-use your connections with multi-factor authentication
    # Uncomment the two lines below
    #ControlMaster auto
    #ControlPath ~/.ssh/tmp/%h_%p_%r

Host grace milgram ruddle
    HostName %h.hpc.yale.edu

Host mccleary
    HostName %h.ycrc.yale.edu
```

!!! warning
    For multiplexing to work, the `~/.ssh/tmp` directory must exist. Create it with `mkdir -p ~/.ssh/tmp`

For more info on ssh configuration, run:

``` bash
man ssh_config
```

## Store Passphrase and Use SSH Agent on macOS

By default, macOS won't always remember your ssh key passphrase and keep your ssh key in the agent for SSH agent forwarding. In order to not repeatedly enter your passphrase and instead store it in your keychain, enter the following command on your Mac (just once):

``` bash
ssh-add -K ~/.ssh/id_rsa
```

Or whatever your private key file is named.

!!! note
    If you use homebrew your default OpenSSH may have changed. To add your key(s) to the system ssh agent, use the absolute path: `/usr/bin/ssh-add`

Then and add the following to your `~/.ssh/config` file (create this file if it doesn't exist, or add these settings to the `Host *.hpc.yale.edu ...` rule if it does).

```
Host *.hpc.yale.edu grace milgram ruddle
    UseKeychain yes
    AddKeystoAgent yes

Host *.ycrc.yale.edu mccleary
    UseKeychain yes
    AddKeystoAgent yes

```

You can view a list of the keys currently in your agent with:

``` bash
ssh-add -L
```
