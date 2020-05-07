# Large Transfers with Globus

For large data transfers both within Yale and to external collaborators, we recommend using Globus. Globus is a file transfer service that is efficient and easy to use. It has several advantages:

* Robust and fast transfers of large files and/or large collections of files.
* Files can be transferred between your computer and the clusters.
* Files can be transferred between Yale and other sites.
* A web and command-line interface for starting and monitoring transfers.
* Access to specific files or directories granted to external collaborators in a secure way.

Globus transfers data between computers set up as "endpoints". The official YCRC endpoints are listed below. Transfers can be to and from these endpoints or those you have defined for yourself with [Globus Connect](#setup-an-endpoint-on-your-computer).

## Cluster Endpoints

We currently support endpoints for the following clusters.

| Cluster                                     | Globus Endpoint |
|---------------------------------------------|-----------------|
| [Farnam](/clusters-at-yale/clusters/farnam) | `yale#farnam`   |
| [Grace](/clusters-at-yale/clusters/grace)   | `yale#grace`    |
| [Ruddle](/clusters-at-yale/clusters/ruddle) | `yale#ruddle`   |

These endpoints provide access to all files you normally have access to, except sequencing data on Ruddle.

## Get Started with Globus

1. In a browser, go to [app.globus.org](https://app.globus.org/).
1. Use the pull-down menu to select Yale and click "Continue".
1. If you are not already logged into CAS, you will be prompted to log in.
    1. [First login only] Do not associate with another account yet unless you are familiar with doing this
    1. [First login only] Select "non-profit research or educational purposes"
    1. [First login only] Click on "Allow" for allowing Globus Web App
1. From the [file manager interface](https://app.globus.org/file-manager) enter the name of the endpoint you would like to browse in the collection field (e.g. yale#farnam)
1. Click on the right-hand side menu option "Transfer or Sync to..."
1. Enter the second endpoint name in the right search box (e.g. another cluster or your personal endpoint)
1. Select one or more files you would like to transfer and click the appropriate start button on the bottom.

## Sharing Data Using Globus

1. From the [file manager interface](https://app.globus.org/file-manager) enter the name of the endpoint you would like to share from in the collection field (e.g. yale#grace)
1. Click the Share button on the right
1. Click on "Add a Shared Endpoint"
1. Next to Path, click "Browse" to find and select the directory you want to share
1. Add other details as desired and click on "Create Share"
1. Click on "Add Permissions -- Share With"
1. Under "Username or Email" enter the e-mail address of the person that you want to share the data with, then click on "Save", then click on "Add Permission"
1. Do not select "write" unless you want the person you are sharing the data with to be able to write to the share.

For more information, please see the [official Globus Documentation](https://docs.globus.org/how-to).

## Setup an Endpoint on Your Computer

You can set up your own endpoint for transferring data to and from your own computer with [Globus Connect](https://www.globus.org/globus-connect). Usually you will want to use Globus Connect Personal.

## Setup a Google Drive Endpoint

See our [Google Drive Documentation](/data/google-drive) for instructions for using Globus to transfer data to EliApps Google Drive.
