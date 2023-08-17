# Multi-factor Authentication

To improve security, access to McCleary requires both a public key and multi-factor authentication (MFA).
We use the same MFA (Duo) as is used elsewhere at Yale.
To get set up with Duo, see these [instructions.](https://cybersecurity.yale.edu/mfa)

You will need upload your [ssh public key to our site](https://sshkeys.ycrc.yale.edu/).
For more info on how to use ssh, please see the [SSH instructions](/clusters-at-yale/access).

Once you've set up Duo and your key is registered, you can log in to McCleary.
Use ssh to connect to your cluster of choice, and you will be prompted for a passcode or to select a notification option.
We recommend choosing Duo Push (option 1).
If you chose this option you should receive a notification on your phone.
Once approved, you should be allowed to continue to log in.

!!!note
    You can set up more than one phone for Duo.
    For example, you can set up your smartphone plus your office landline.
    That way, if you forget or lose your phone, you can still authenticate.
    For instructions on how to add additional phones go [here](https://guide.duo.com/enrollment#add-or-manage-devices).

## Connection Multiplexing and File Transfers with DUO MFA

Some file transfer clients attempt new and sometimes multiple concurrent connections to transfer files for you.
When this happens, you will be asked to Duo authenticate for each connection.

### SSH Config File
On macOS and Linux-based systems setting up a [config file](/clusters-at-yale/access/advanced-config) lets you re-uses your authenticated sessions for command-line tools and tools that respect your ssh configuration. 
An example config file is shown below which enables SSH multiplexing (`ControlMaster`) by caching connections in a directory (`ControlPath`) for a period of time (2h, `ControlPersist`). 

```

Host *.ycrc.yale.edu mccleary grace milgram
    User NETID
    # Uncomment below to enable X11 forwarding without `-Y`
    #ForwardX11 yes
    # To re-use your connections with multi-factor authentication
    ControlMaster auto
    ControlPath ~/.ssh/tmp/%h_%p_%r
    ControlPersist 2h

Host mccleary grace milgram
    HostName %h.ycrc.yale.edu
```

!!! warning
    For multiplexing to work, the `~/.ssh/tmp` directory must exist. Create it with `mkdir -p ~/.ssh/tmp`


### CyberDuck
CyberDuck's interface with MFA can be stream-lined with a few additional configuration steps.
Under `Cyberduck > Preferences > Transfers > General` change the setting to "Use browser connection" instead of "Open multiple connections".

When you connect type one of the following when prompted with a "Partial authentication success" window.

* "push" to receive a push notification to your smart phone (requires the Duo mobile app)
* "sms" to receive a verification passcode via text message
* "phone" to receive a phone call

### MobaXTerm

MobaXTerm is able to cache MFA connections to reduce the frequency of push notifications.
Under `Settings > SSH > Advanced SSH settings` set the ssh browser type to `scp (enhanced speed)` as seen here:

[MobaXTerm SSH Settings](/img/mobaxterm_mfa.png)

### WinSCP

Similarly, WinSCP can reuse existing SSH connections to reduce the frequency of push notifications. 
Under `Options > Preferences > Background (under Transfer)` and:

* Set `Maximal number of transfers at the same time:` to 1
* Check the `Use multiple connections for single transfer` box
* Click `OK` to save settings


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
