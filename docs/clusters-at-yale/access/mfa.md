# Multi-factor Authentication

To improve security, access to Ruddle requires both a public key and multi-factor authentication (MFA). We use the same MFA (Duo) as is used elsewhere at Yale. To get set up with Duo, see these [instructions.](https://cybersecurity.yale.edu/topic/use-yales-multifactor-authentication-mfa-service)

You will need upload your [ssh public key to our site](https://sshkeys.hpc.yale.edu/). For more info on how to use ssh, please see the [SSH instructions](/clusters-at-yale/access).

Once you've set up Duo and your key is registered, you can log in to Ruddle. Use ssh to connect to your cluster of choice, and you will be prompted for a passcode or to select a notification option. We recommend choosing Duo Push (option 1). If you chose this option you should receive a notification on your phone. Once approved, you should be allowed to continue to log in.

!!!note
    You can set up more than one phone for Duo. For example, you can set up your smartphone plus your office landline. That way, if you forget or lose your phone, you can still authenticate. For instructions on how to add additional phones go [here](http://its.yale.edu/sites/default/files/imce/pdfs/MFA%20Adding%20a%20new%20device%2008312015.pdf).

## File Transfer and Duo MFA

Some file transfer clients attempt new and sometimes multiple concurrent connections to transfer files for you. When this happens, you will be asked to Duo authenticate for each connection. Setting up a [config file](/clusters-at-yale/access/advanced-config) lets you re-uses your authenticated sessions for command-line tools and tools that respect your ssh configuration. For CyberDuck, see our [section on the Transfer Data page](/data/transfer/#cyberduck-on-ruddle).

## Troubleshoot MFA

If you are having problems initially registering Duo, please contact the [Yale ITS Helpdesk](https://yale.service-now.com/it?id=get_help).

If you have successfully used MFA connect to a cluster before, but cannot now, first please check the following:

* Test MFA using [http://access.yale.edu](http://access.yale.edu)
* Verify that your ssh client is using the correct login node
* Verify you are attempting to connect from a Yale machine or via the proper VPN

If all of this is true, please [contact us](/#get-help). Include the following information (and anything else you think is helpful):

* Your netid
* Have you ever successfully used ssh and Duo to connect to a cluster?
* How long have you been having problems?
* Where are you trying to connect from? (fully qualified hostname/IP, if possible)
* Are you using a VPN?
* What is the error message you see?
