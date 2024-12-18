# VSCode

[Visual Studio Code](https://code.visualstudio.com) is a popular development tool that is widely used by our researchers.
While there are several extensions that allow users to connect to remote servers over SSH, these are imperfect and often drop connection. 
Additionally, these remote sessions connect to the clusters' login nodes, where resources are limited.

## Code Server

The Code Server app launches VSCode in a job on a compute node and opens in your web browser, providing a stable connection that is not subject to the strict limits on the login.
To get started, connect to one of cluster [Web Portals](/clusters-at-yale/access/ood) and choose Code Server from the Interactive Apps menu in the portal and then follow the instructions for [launching an interactive app](/clusters-at-yale/access/ood/#launch-an-interactive-app).