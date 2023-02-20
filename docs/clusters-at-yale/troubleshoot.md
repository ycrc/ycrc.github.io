# Troubleshoot Login

## Checklist

If you are having trouble logging into a cluster, please use the checklist below to check for common issues:

- [ ] Make sure you have submitted an [account request](https://research.computing.yale.edu/support/hpc/account-request) and have gotten word that we created your account for the cluster.
- [ ] Make sure that the cluster is online in the [System Status](http://research.computing.yale.edu/system-status) page.
- [ ] Check the hostname for the cluster. See the [clusters page](/clusters) for a list.
- [ ] Verify that your [ssh keys](/clusters-at-yale/access/#what-are-ssh-keys) are setup correctly
    - [ ] Check for your public key in the [ssh key uploader](https://sshkeys.hpc.yale.edu/). If you recently uploaded one, it will take a few minutes appear on the cluster. 
    - [ ] If you are using [macOS or Linux](/clusters-at-yale/access/#macos-and-linux), make sure your private key is in `~/.ssh`.
    - [ ] If you are [using Windows](/clusters-at-yale/access/#windows), make sure you have pointed MobaXterm to your private ssh key (ends in .pem)
    - [ ] If you are asked for a passphrase when logging in, this is the ssh key passphrase you set when first creating your key pair. If you have forgotten this passphrase, you need to create a new key pair and upload a new public key.
- [ ] Make sure your computer is either on Yale's campus network (ethernet or YaleSecure wireless) or [Yale's VPN](/clusters-at-yale/access/vpn/).
    - [ ]  If you get an error like `could not resolve hostname` you may have lost connection to the Yale network. If you are sure you have not, make sure that you are also using the Yale DNS servers (130.132.1.9,10,11).
- [ ] Your home directory should only be writable by you. If you recently modified the permissions to your home directory and can't log in, [contact us](/#get-help) and we can fix the permissions for you.
- [ ] If you are using [Ruddle](/clusters/ruddle), we require Duo MFA for every login. If following our [MFA Troubleshooting steps](/clusters-at-yale/access/mfa/#troubleshoot-mfa) doesn't  work, contact the [ITS Help Desk](https://yale.service-now.com/it?id=get_help).

If none of the above solve your issue, please [contact us](/#get-help) with your netid and the cluster you are attempting to connect to.


## Common SSH Errors

#### Permission denied (publickey)

This message means that the clusters don't (yet) have they key you are using to authenticate. Make sure you have an account on the cluster you're connecting, that you have [created an ssh key pair](/clusters-at-yale/access/#what-are-ssh-keys), and uploaded the [public key](https://sshkeys.hpc.yale.edu/). If you recently uploaded one, it will take a few minutes appear on the cluster.

#### REMOTE HOST IDENTIFICATION HAS CHANGED!

If you are seeing the following error:

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
....
Offending key in /home/user/.ssh/known_hosts:34
...

```

This usually means that the keys that identify the cluster login nodes have changed. This can be the result of system upgrades on the cluster. It could also mean someone is trying to intercept your ssh session. Please [contact us](/#get-help) if you receive this error.

If the host keys have indeed changed on the server you are connecting to, you can edit `~/.ssh/known_hosts` and remove the offending line. In the example above, you would need to delete line 34 in `~/.ssh/known_hosts` before you re-connect.
