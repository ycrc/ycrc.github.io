# Access from Off Campus (VPN)

Yale's clusters can only be accessed on the Yale network. Therefore, in order to access a cluster from off campus, you will need to first connect to Yale's VPN. More information about Yale's VPN can be found on the [ITS website](https://yale.service-now.com/it?id=service_offering&sys_id=c4684dcd6fbb31007ee2abcf9f3ee4f2).

## VPN Software
### Windows and macOS

We recommend the Cisco AnyConnect VPN Client, which can be downloaded from the [ITS Software Library](https://yale.onthehub.com/WebStore/ProductSearchOfferingList.aspx?srch=cisco).

### Linux

On Linux, you can use [openconnect](http://www.infradead.org/openconnect) to connect to one of Yale's VPNs. If you are using the standard Gnome-based distros, use the commands below to install.

Ubuntu/Debian

``` bash
sudo apt install network-manager-openconnect-gnome
```

Fedora/CentOS

``` bash
sudo yum install NetworkManager-openconnect
```

#### Using a GUI

Right-click on the NetworkManager icon and select "Edit connections...".

Click the "+" at the bottom to add a new connection.

![New connection.](/img/NewLinuxConnection.png){: .large}

For connection type, choose "Cisco AnyConnect or OpenConnect (Openconnect)".

![Select connection.](/img/CreateLinuxVPN.png){: .medium}

Choose a helpful name for the connection (e.g., "Yale"), and fill out the fields as shown.

![Configure connection.](/img/ConfigureLinuxVPN.png){: .medium}

Note the activation and specification of the Trojan scanner script, which should have been
installed along with OpenConnect.

Save this connection, and it will be available from the NetworkManager app's pop-up menu
under "VPN connections".

#### Using the command line

``` bash
nmcli con add type vpn con-name Yale-VPN -- vpn-type openconnect vpn.data "gateway=access.yale.edu,protocol=anyconnect,useragent=AnyConnect Linux_64 4.10.07061"
```
## Connect via VPN

You will need to connect via the VPN client using the profile "access.yale.edu".

![VPN client.](/img/vpn1.png){: .medium}

### Multi-factor Authentication (MFA)

Authentication for the VPN requires multi-factor authentication via Duo in addition to your normal Yale credentials (email address  and netid password). After you select "Connect" in the above dialog box, it will launch a web page with a prompt to login with your email address, netid password and MFA method.

You can click "Other options" to choose your authentication method. 

* If you choose "Duo Push", simply tap "Approve" on your mobile device.
* If you choose "Duo Mobile passcode", enter the passcode from the Duo Mobile app.
* If you choose "Phone call", follow the prompts when you are called.

Once you successfully authenticate with MFA, you will be connected to the VPN and should be able to log in the clusters via SSH and Open OnDemand as usual.

More information about MFA at Yale can be found on the [ITS website](https://cybersecurity.yale.edu/mfa).
