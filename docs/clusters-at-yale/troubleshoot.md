# Troubleshoot Login

If you are having trouble logging in, please check the following:

1. Check the status page to make sure that your cluster is online: [System Status](http://research.computing.yale.edu/system-status).
1. Accounts are only created for you on the clusters as you requested them. To get access to additional clusters, submit another [account request](https://research.computing.yale.edu/account-request).
1. Verify that you are attempting to ssh to the correct hostname. Please see the [cluster page](/clusters-at-yale/clusters) for a list of login addresses.
1. Verify that your ssh keys are setup correctly. Make sure your public key is uploaded to the [ssh key uploader](http://gold.hpc.yale.internal/cgi-bin/sshkeys.py). If you are on Windows, make sure you have pointed MobaXterm to your private ssh key and if you are on macOS or Linux, your private key needs to be in `${HOME}/.ssh`.
1. We use ssh keys to authenticate logins to the clusters, and not NetID passwords. If you are asked for a "passphrase" upon logging in, this is the ssh key passphrase you configured when first creating your key. If you have forgotten your passphrase, you will need to create and upload a new ssh key pair (see our [SSH Guide](/clusters-at-yale/access)).
1. Make sure you are accessing the cluster from either Yale's campus networks (ethernet or YaleSecure for wireless) or [Yale's VPN](https://yale.service-now.com/it?id=service_offering&sys_id=c4684dcd6fbb31007ee2abcf9f3ee4f2) if you are off-campus.
1. The home directory should only be write-able by your NetID. If you recently modified the permissions to your home directory, contact us at [hpc@yale.edu](mailto:hpc@yale.edu) and we can fix the permissions for you.
1. If you get an error like "could not resolve hostname" make sure that you are using the Yale DNS servers (130.132.1.9,10,11). External DNS servers do not list our clusters.
1. If you are using Ruddle, they require Duo MFA on your smartphone. If Duo is not working for you, try testing it on this ITS site: [http://access.yale.edu/mfa](http://access.yale.edu/mfa). If that doesn't work, contact the Yale Help Desk.

If all of the above check out ok, please [contact us](mailto:hpc@yale.edu) and we will investigate further. Please include your netid and the cluster you are attempting to connect to in your email.

* * *

## "REMOTE HOST IDENTIFICATION HAS CHANGED!" Warning

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

This error means that the host keys on the cluster have changed. This may be the result of system upgrades on the cluster. It could also mean someone is trying to intercept your ssh session. Please [contact us](mailto:hpc@yale.edu) if you receive this error.

If the host keys have indeed changed on the server you are connecting to, you can edit `~/.ssh/known_hosts` and remove the offending line. In the example above, line 34 in `~/.ssh/known_hosts` would have to be deleted before you re-connect.