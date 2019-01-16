# Sample Config File

The following configuration is an example ssh client configuration file (linux and mac only) specific to our clusters. It will allow you to use tab completion of the clusters, sans the .hpc.yale.edu suffixes (e.g. `ssh farnam` will now work). It will also allow you to re-use and multiplex authenticated sessions. Practically this means clusters that require [Duo MFA](/node/10546/) will not need you to re-authenticate, as you use the same ssh connection to host multiple sessions. If you attempt to close your first connection with others running, it will wait until all others are closed.

For this to work, you need to create the directory `~/.ssh/tmp`:

``` bash
mkdir -p ~/.ssh/tmp
```

Then take the text below and replace `NETID` with your yale netid. Lines that begin with `#` will be ignored. Save this file (or add it to the file that already exists) in `~/.ssh/config`

```
#re-use your connections with multi-factor authentication (Ruddle)
ControlMaster auto
ControlPath ~/.ssh/tmp/%h_%p_%r

# If you use a ssh key that is named something other than id_rsa, 
# specify it like this
# IdentityFile ~/.ssh/other_key_rsa 

#uncomment the ForwardX11 options to enable X11 Forwarding by default (no -Y necessary)
Host farnam
     HostName farnam.hpc.yale.edu
     User NETID 
#     ForwardX11 yes

Host ruddle
     HostName ruddle.hpc.yale.edu
     User NETID 
#     ForwardX11 yes

Host grace
     HostName grace.hpc.yale.edu
     User NETID 
#     ForwardX11 yes

Host omega
     Hostname omega.hpc.yale.edu
     User NETID 
#     ForwardX11 yes

```

For more info, run:

``` bash
man ssh_config
```