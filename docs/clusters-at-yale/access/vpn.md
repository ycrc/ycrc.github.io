# Access from Off Campus (VPN)

Yale's clusters can only be accessed on the Yale network. Therefore, in order to access a cluster from off campus, you will need to first connect to Yale's VPN. We recommend the Cisco AnyConnect VPN Client, which can be downloaded from the [ITS Software Library](http://software.yale.edu/software/cisco-vpn-anyconnect).

More information about Yale's VPN can be found on the [ITS website](https://yale.service-now.com/it?id=service_offering&sys_id=c4684dcd6fbb31007ee2abcf9f3ee4f2).

## Connect via VPN

You will need to connect via the VPN client using the profile "access.yale.edu".

![VPN client.](/img/vpn1.png){: .medium}

### Multi-factor Authentication (MFA)

Authentication for the VPN requires multi-factor authentication via Duo in addition to your normal Yale credentials (netid and password). After you select "Connect" in the above dialog box, you will be presented with a new prompt to enter your netid, password and an MFA method.

![VPN with MFA.](/img/vpn2.png){: .medium}

Depending on what you choose you will be prompted to authenticate via a second authentication method.

* If you type "push", simply tap "Approve" on your mobile device.
* If you type "sms" you will receive a text message with your passcode. Enter the passcode you received to authenticate.
* If you type "phone", follow the prompts when you are called.

Once you successfully authenticate with MFA, you will be connected to the VPN and should be able to log in the clusters via SSH as usual.

More information about MFA at Yale can be found on the [ITS website](https://cybersecurity.yale.edu/topic/use-yales-multifactor-authentication-mfa-service).