# VSCode

[Visual Studio Code](https://code.visualstudio.com) is a popular development tool that is widely used by our researchers.


!!!warning
    To protect the security of the data, the use of [Cursor](https://cursor.com/), [GitHub Copilot](https://github.com/features/copilot) or any externally hosted AI Coding agents on the Milgram cluster is not permitted.

## Choosing a Method

There are several ways to use Visual Studio Code with the YCRC clusters, depending on your specific application and/or preferences:

- **[Code Server](#code-server)** (Recommended): A web-based VSCode instance running on a compute node, accessed through your browser via Open OnDemand. This is the recommended method for most users as it provides a stable connection and requires no local configuration.

- **[Remote Tunnel](#remote-tunnel-advanced-users)**: For advanced users who want to use their local VSCode installation. Uses GitHub authentication to tunnel to a compute node. **Note: Not permitted on Milgram due to security requirements.**

- **[Remote SSH](#remote-ssh-via-compute-node-advanced-users)**: An alternative for users who want to use their local VSCode installation but cannot use the Remote Tunnel method. Requires SSH configuration and connecting through login nodes to compute nodes.

## Code Server

**This is the recommended method for most users.**

The Code Server app launches an open source version of VSCode in a job on a compute node and opens in your web browser.

### Getting Started

1. Connect to one of the cluster [Web Portals](/clusters-at-yale/access/ood)
2. Choose "Code Server" from the Interactive Apps menu
3. Follow the instructions for [launching an interactive app](/clusters-at-yale/access/ood/#launch-an-interactive-app)
4. Once the job starts, click "Connect to Code Server" to open VSCode in your browser

This method works on all YCRC clusters.

## Remote Tunnel

This method allows you to use your local VSCode installation and connect to a VSCode server running on a cluster compute node via GitHub authentication. This is suitable for advanced users who prefer to use their desktop VSCode with their own extensions and settings.

!!!warning
    Due to data security requirements, the Remote Tunnel method is not permitted on Milgram.

!!! note "Note"
    We do not recommend connecting your Remote Tunnel session directly to the login nodes, as this can result in instability and undue burden on the login nodes. Please follow the below instructions to connect to a compute node.

### Setup Instructions

1. Create a vscode server batch script called `vscode_slurm.sh` and submit it to the queue with `sbatch vscode_slurm.sh`. The script source code is below.

2. After this script successfully starts running, check the last line of the logfile `vscode_slurm.txt` (in the directory you submitted the job from). The last line will look like:
```
To grant access to the server, please log into https://github.com/login/device and use code XXXX-XXXX
```

3. Open your web browser and navigate to the GitHub device login URL shown in the log file. Enter the code to authenticate.

4. Run your local VSCode app. Then, connect to the server from within the app as follows:

    - Press `F1` or `Cmd/Ctrl+Shift+P` to open the Command Palette
    - Type "Remote-Tunnel: Connect to Tunnel" and select it
    - Select the "GitHub" option for authentication, and log in if needed.
    - Select the tunnel listed, typically by its hostname.
    - VSCode will connect through a secure tunnel to the compute node and automatically start the VSCode server


5. Terminate your VSCode batch job when you are done working for that session using `scancel [JOBID]`.

### vscode_slurm.sh Script

!!!warning
    Only submit VSCode jobs to devel partitions (such as `devel` or `gpu_devel`). VSCode jobs found in other partitions may be terminated without notice. Always terminate your VSCode session when you are done using `scancel` to free up resources for other users.

```bash
#!/bin/bash

#SBATCH --partition=devel
#SBATCH -t 6:00:00
#SBATCH -c 1
#SBATCH --mem=10G
#SBATCH --output=vscode_slurm.txt

# vscode_slurm.sh

# Usage:
# sbatch vscode_slurm.sh

# After this script successfully starts running, use the last line of the
# logfile 'vscode_slurm.txt' (in the directory you submitted the job from)
# to set up a connection from the cluster to your own VSCode app on a remote computer.
# An example last line will look like:

######################
# vscode_slurm.txt
######################
# ...
# To grant access to the server, please log into https://github.com/login/device and use code XXXX-XXXX
######################

module load VSCode
code tunnel
```

!!! note "Note"
    You can set a custom name for your tunnel by adding the `--name` option to the `code tunnel` command in the script. For example:
    ```bash
    code tunnel --name bouchet-vscode
    ```

## Remote SSH via Compute Node (Advanced Users)

This method allows you to use your local VSCode installation with the Remote-SSH extension to connect directly to a compute node. This is an alternative for users who want to use their local VSCode but cannot or prefer not to use the Remote Tunnel method with GitHub authentication.

!!! note "Note"
    Do not connect directly to login nodes with VSCode Remote-SSH. VS Code can initiate computationally expensive processes (compilers, language servers, etc.) that put undue burden on the login nodes where resources are limited. Always connect to a compute node as described below.

### Prerequisites

- VSCode installed on your local machine
- The [Remote-SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) installed in VSCode

### Method 1: Using salloc for Interactive Sessions

1. **Request a compute node interactively:**
   ```bash
   salloc --partition=devel --time=6:00:00 --cpus-per-task=1 --mem=10G
   ```

2. **Once the job is allocated, note the compute node hostname** by running:
   ```bash
   hostname
   ```
   This will return something like `r209u11n04.bouchet.ycrc.yale.edu`, 
`a11231u01n01.mghpcc.ycrc.yale.edu`, etc.

3. **Configure your local SSH setup** (see SSH Configuration section below).

4. **Connect from VSCode** using the Remote-SSH extension.

5. **Keep your terminal session open** - if you exit the salloc session, the compute node allocation will end and your VSCode connection will be lost.

### Method 2: Using a Batch Job

!!!warning
    Only submit VSCode jobs to devel partitions (such as `devel` or `gpu_devel`). VSCode jobs found in other partitions may be terminated without notice. Always terminate your VSCode session when you are done using `scancel` to free up resources for other users.

1. **Create a batch script** called `vscode_ssh.sh`:
   ```bash
   #!/bin/bash
   #SBATCH --partition=devel
   #SBATCH --time=6:00:00
   #SBATCH --cpus-per-task=1
   #SBATCH --mem=10G
   #SBATCH --output=vscode_ssh-%J.log

   # Print the hostname to the log file
   echo "VSCode SSH session ready on node: $(hostname -s)"
   echo "Full hostname: $(hostname)"

   # Keep the job alive
   # VSCode will connect via SSH and start its server automatically
   sleep 6h
   ```

2. **Submit the job:**
   ```bash
   sbatch vscode_ssh.sh
   ```

3. **Check the log file** to get the compute node hostname:
   ```bash
   cat vscode_ssh-[JOBID].log
   ```

4. **Configure your local SSH setup** with the compute node name (see below).

5. **Terminate your VSCode batch job when you are done working** for that session using `scancel [JOBID]`.

### SSH Configuration

You need to configure SSH on your local machine to connect through the login node to the compute node.

#### macOS and Linux

Add the following to your `~/.ssh/config` file on your **local machine**:

```ssh-config
# Connection to cluster login node (example for Grace cluster)
Host grace
    HostName grace.ycrc.yale.edu
    User YOUR_NETID
    IdentityFile ~/.ssh/SSH_KEY_FILE

# Connection to compute node via login node
Host grace-compute
    HostName COMPUTE_NODE_NAME
    User YOUR_NETID
    IdentityFile ~/.ssh/SSH_KEY_FILE
    ProxyJump grace
```

Replace:

- `YOUR_NETID` with your Yale NetID  
- `COMPUTE_NODE_NAME` with the full hostname from step 2 or 3 (e.g., `r209u10n01.grace.ycrc.yale.edu`)  
- `SSH_KEY_FILE` with the path to the SSH key file you created for the cluster (e.g., `~/.ssh/id_rsa`)  

Modify the `Host` and `HostName` as needed for the cluster you are using.

#### Windows

Add the following to your SSH config file on your **local Windows machine**. The config file is typically located at `C:\Users\YOUR_USERNAME\.ssh\config` (you may need to create this file if it doesn't exist):

```ssh-config
# Connection to cluster login node
Host grace
    HostName grace.ycrc.yale.edu
    User YOUR_NETID
    IdentityFile C:\Users\YOUR_USERNAME\.ssh\SSH_KEY_FILE

# Connection to compute node via login node
Host grace-compute
    HostName COMPUTE_NODE_NAME
    User YOUR_NETID
    IdentityFile C:\Users\YOUR_USERNAME\.ssh\SSH_KEY_FILE
    ProxyJump grace
```

Replace:

- `YOUR_USERNAME` with your Windows username  
- `YOUR_NETID` with your Yale NetID  
- `COMPUTE_NODE_NAME` with the full hostname from step 2 or 3 (e.g., `r209u10n01.grace.ycrc.yale.edu`)  
- `SSH_KEY_FILE` with the name of your SSH key file (e.g., `id_rsa`)  

Modify the `Host` and `HostName` as needed for the cluster you are using.

!!! tip "Creating the config file on Windows"
    If the `.ssh` folder or `config` file doesn't exist, you can create it:

    1. Open PowerShell or Command Prompt
    2. Run: `mkdir $env:USERPROFILE\.ssh` (if the folder doesn't exist)
    3. Run: `notepad $env:USERPROFILE\.ssh\config`
    4. This will open Notepad where you can paste the configuration and save the file

### Connecting from VSCode

1. Open VSCode on your local machine
2. Press `F1` or `Cmd/Ctrl+Shift+P` to open the Command Palette
3. Type "Remote-SSH: Connect to Host" and select it
4. Choose `grace-compute` (or whatever you named the host in your config)
5. At this point, at least on some machines (we have seen this on Windows but not on Apple laptops), VSCode may appear to get stuck with the message 'Setting up SSH Host bouchet-compute (details)' in the bottom of the window. This means you need to authenticate, but you will need to find the hidden prompt first.

    To do this, click on the blue highlighted 'details' to reveal a set of tabs at the bottom of the window, and click on the 'TERMINAL' tab. There you can respond to the Duo two-factor prompt to complete the connection.

6. VSCode will then connect through the login node to your compute node and automatically start the VSCode server

When VSCode connects, it will automatically install and start the VSCode server on the compute node. Your files, terminal, and all VSCode features will be running on the compute node. Remember to terminate your VSCode batch job when you are done working** for that session using `scancel [JOBID]`







