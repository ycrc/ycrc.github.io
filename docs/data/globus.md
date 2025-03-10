# Large Transfers with Globus

For large data transfers both within Yale and to external collaborators, we recommend using Globus. Globus is a file transfer service that is efficient and easy to use. It has several advantages:

* Robust and fast transfers of large files and/or large collections of files.
* Files can be transferred between your computer and the clusters.
* Files can be transferred between Yale and other sites.
* A web and command-line interface for starting and monitoring transfers.
* Access to specific files or directories granted to external collaborators in a secure way.

Globus transfers data between computers set up as "endpoints". The official YCRC endpoints are listed below. Transfers can be to and from these endpoints or those you have defined for yourself with [Globus Connect](#setup-an-endpoint-on-your-computer).

!!! warning "Course Accounts"
    Globus does not work for course accounts (`<course_id>_<netid>`).
    Please try the other transfer methods listed in our [Transfer documentation](/data/transfer/) instead.


## Cluster Endpoints

We currently support endpoints for the following clusters.

| Cluster                        | Globus Endpoint     |
|--------------------------------|---------------------|
| [Grace](/clusters/grace)       | `Yale CRC Grace`        |
| [McCleary](/clusters/mccleary) | `Yale CRC McCleary` |
| [Milgram](/clusters/milgram)   | `Yale CRC Milgram`  |
| [Hopper Low Risk](/clusters/milgram)   | `Yale CRC Hopper Low Risk`  |

For Grace and McCleary, these endpoints provide access to all files you normally have access to.

For security reasons, Milgram Globus uses a staging area (`/gpfs/milgram/globus/$NETID`). 
Once uploaded, data should be moved from this staging area to its final location within Milgram.
Files in the staging area are purged after 21 days.

For Hopper, the Low Risk endpoint mounts a staging area. Once you have staged your data, please submit [this form](https://forms.gle/YigxQdbvobaH7YDT6) to have the files transferred to Hopper.
If your data is larger than 100G, please submit your request without uploading any data to Globus and we will 

## Get Started with Globus

### Authenticate

1. In a browser, go to [app.globus.org](https://app.globus.org/).
1. Use the pull-down menu to select Yale and click "Continue".
1. If you are not already logged into CAS, you will be prompted to log in.
    1. [First login only] Do not associate with another account yet unless you are familiar with doing this
    1. [First login only] Select "non-profit research or educational purposes"
    1. [First login only] Click on "Allow" for allowing Globus Web App

### Transfer Between Endpoints

1. From the [file manager interface](https://app.globus.org/file-manager) enter the name of the endpoint you would like to browse in the collection field (e.g. Yale CRC Grace)
1. Click on the right-hand side menu option "Transfer or Sync to..."
1. Enter the second endpoint name in the right search box (e.g. another cluster or your personal endpoint)
1. Select one or more files you would like to transfer and click the appropriate start button on the bottom.
2. To complete a partial transfer, you can click the "sync" checkbox in the Transfer Setting window on the Globus page, and then Globus should resume the transfer where it left off.

### Upload or Download Directly from Globus Web App

From the [file manager interface](https://app.globus.org/file-manager) enter the name of the endpoint you would like to browse in the collection field (e.g. Yale CRC Hopper Low Risk).
You will need to be on the Yale VPN is you are off campus or connecting to a secure cluster.

#### Upload
1. In the main pane, navigate to the destination for your files
1. To Upload, select "Upload" in the sidebar and browse to the file or folder you would like to upload

#### Download
1. In the main pane, navigate to your file
1. Right-Click and select "Download"

### URL links to your Globus files
To obtain a direct URL (HTTPS) link to a file in a Globus collection, right click and select "Get Link". Then click on the copy icon to the right of the option "access the selected file directly". Note that this link will only work for Globus users with access permission to that file.

### Manage Your Endpoints

To manage your endpoints, such as delete an endpoint, rename it, or share it with additional people (be aware, they will be able to access your storage), go to [Manage Endpoint](https://app.globus.org/endpoints) on the Globus website.

## Set Up an Endpoint on Your Computer

You can set up your own endpoint for transferring data to and from your own computer with [Globus Connect Personal](https://www.globus.org/globus-connect). 

To transfer or share data between two personal endpoints, you will need to request access to the YCRC's Globus Plus subscription on [this page](https://app.globus.org/groups/8f3fced6-4318-11e3-9f63-12313809f035/join).

## Set Up a [Microsoft OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage) Endpoint

1. Click on the following link: [Globus OneDrive Endpoint](https://app.globus.org/file-manager?origin_id=923b3fbe-ffd2-4a8e-b4ad-be207fd33faa)
1. Log into Globus, if needed.
1. The first time you log into the endpoint, you will be asked ot grant access to your OneDrive account.  Click to allow access and be taken through the approval process.
1. After granting approval, you will be able to access the top level of your Yale OneDrive via the Globus Collection "Yale OneDrive".

## Set Up a [Dropbox](https://www.dropbox.com) Endpoint

1. Click on the following link: [Globus Dropbox Endpoint](https://app.globus.org/file-manager?origin_id=ced0b3b0-e7f2-4ffb-aa09-418f7c42a38d)
1. Log into Globus, if needed.
1. The first time you log into the endpoint, you will be asked to grant access to your DropBox account.  Click to allow access and be taken through the approval process.
1. After granting approval, you will be able to access the top level of your DropBox storage via the Globus Collection "Yale Dropbox".

## Set Up a [Google Drive](https://www.google.com/drive/) Endpoint

The Globus connector is configured to only allow data to be uploaded into EliApps (Yale's GSuite for Education) Google Drive accounts. If you don't have an EliApps account, request one as described above.

1. Click on the following link: [Globus Google Drive Endpoint](https://app.globus.org/file-manager?origin_id=28ae8ae7-b2c6-47b4-badc-da9c1cab1e6e)
1. Log into Globus, if needed.
1. The first time you login to the Globus Google Drive endpoint, you will be asked to grant access to your Google Drive. Click to allow access and be taken through the approval process.
1. You may see your Yale EliApps account expressed in an uncommon format, such as netid@yale.edu@accounts.google.com. This is normal, and expected.
1. After granting approval, you will be able to access your Google Drive via the Globus Collection "YCRC Globus Google Drive Collection". The default view is "/My Drive". To see "/Team Drives" and other Google Drive features use the "up one folder" arrow icon in the File Manager.

!!! note 
    There are "rate limits" to how much data and how many files you can transfer in any 24 hours period. If you have hit your rate limit, Globus should automatically resume the transfer during the next 24 hour period. You see a "Endpoint Busy" error during this time.

    Google has a 400,000 file limit per [Shared Drive](/data/google-drive), so if you are archiving data to Google Drive, it is better to compress folders that contain lots of small files (e.g. using [tar](/resources/online-tutorials)) before transferring. 

In our testing, we have seen up to 10MB/s upload and 100MB/s download speeds.

## Setup a S3 Endpoint

We support creating Globus S3 endpoints. To request a Globus S3 Endpoint, please [contact YCRC](https://docs.ycrc.yale.edu/#web-and-email-support). Please include in your request:

- S3 bucket name
- The [Amazon Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) for that bucket
- An initial list of Yale NetIDs who should be able to access the bucket

!!! warning
    Please DO NOT send us the Amazon login credentials through an insecure method such as email or our ticketing system.

After we have created your Globus S3 endpoint, you will be able to further self-serve you own access controls with the Globus portal.


