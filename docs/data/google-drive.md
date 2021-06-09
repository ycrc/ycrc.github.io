# Google Drive

Through Yale Google Apps for Education (EliApps), researchers have free Google Drive storage with very few limits on storage. The Globus Google Drive connector allows you to create a Globus endpoint that allows you to use the Globus infrastructure to transfer data into your Google Drive account. As always, no sensitive data (e.g. ePHI, HIPAA) is allowed in Google Drive storage.

!!! warning
    We have upgraded our Globus Google Drive connector. Existing Globus Google Drive endpoints (created prior to April 29th, 2021) will be decommissioned on Monday, July 12, 2021, at which point they will stop working.  Please [follow the instructions below](/data/google-drive/#globus-google-drive-connector) to setup a new endpoint on the upgraded system. 

    Once you have created a new endpoint, you may remove the old one at [app.globus.org/endpoints?scope=administered-by-me](app.globus.org/endpoints?scope=administered-by-me).

## EliApps

If your Yale email account is already an EliApps account (Gmail), then you are all set. If your Yale email is in Microsoft Office365, send an email to the [ITS helpdesk](mailto:helpdesk@yale.edu) requesting a "no-email EliApps account". Once it is created you can login to Google Drive using your EliApps account name, which will be of the form `netid@yale.edu`. The Globus connector is configured to only allow data to be uploaded into EliApps Google Drive accounts.

### Google Shared Drives (formerly Team Drive)

[Shared Drives](https://gsuite.google.com/learning-center/products/drive/get-started-team-drive/#!/) is an additional feature for EliApps that is available by request only (at the moment). A Shared Drive is a Google Drive space that solves a lot of ownership and permissions issues present with traditional shared Google Drive folder. Once you create a Shared Drive, e.g. for a project or research group, any data placed in that Drive are owned by the drive and the permission (which accounts can own or access the data) can be easily managed from the Shared Drive interface by drive owners. With Shared Drive, you can be sure the data will stay with research group as students and postdocs come and go. To request Shared Drive, first make sure you have an EliApps account (see above) then [contact us](/#get-help). We will work with ITS on your behalf to enable the feature. Although they don't have a total size quota, there are [limits for Google Shared Drives](https://support.google.com/a/answer/7338880?hl=en). Some are listed below.

!!! warning
     To keep file counts low (and for easier data retrieval) we *highly* recommended that you archive your data using zip or [tar](/online-tutorials/#how-create-and-extract-a-tar-or-targz-archive).

| Limit type                                | Limit   |
|-------------------------------------------|---------|
| Number of files and folders               | 400,000 |
| Daily upload cap                          | 750 GiB |
| Max individual file size                  | 5 TiB   |
| Max number of nested folders              | 20      |

### Local File Access

You can upload and access your data using the web portal and sync data with your local machines via the Google File Stream software. For sync with your local machine, install [Google File Stream](https://www.google.com/drive/download/). Select the Download button on the left side under “Business” and authenticate with your EliApps account. You will see Google Drive mounted as an additional drive on your machine.

### Rclone

You can also transfer data using the command line utility [Rclone](/clusters-at-yale/data/transfer/#rclone). Rclone can be used to transfer data to any Google Drive account.

## Globus Google Drive Connector

The Globus connector is configured to only allow data to be uploaded into EliApps (Yale's GSuite for Education) Google Drive accounts. If you don't have an EliApps account, request one as described above.

### Set Up Your Endpoint

1. To set up your Globus Google Drive endpoint, click on the following link: [Setup Globus Google Drive Endpoint](https://app.globus.org/file-manager?origin_id=28ae8ae7-b2c6-47b4-badc-da9c1cab1e6e)
1. Log into Globus, if needed.
1. The first time you login to the Globus Google Drive endpoint, you will be presented with a permissions approval page. If you are ok with the Connector manipulating your files through Globus (which is required), click the Allow button.
1. You may see your Yale EliApps account expressed in an uncommon format, such as netid@yale.edu@accounts.google.com. This is normal, and expected.
1. After your approvals you will be directed to the Globus File Manager, with the default view of "/My Drive". To see "/Team Drives" and other Google Drive features use the "up one folder" arrow icon in the File Manager.

### Using Your Endpoint

On the [Globus Transfer](https://app.globus.org/file-manager) page, select an endpoint for each side of your transfer. To transfer to or from your Google Drive, simply search in the Endpoint field for the name of the Endpoint (e.g. "YCRC Globus Google Drive Collection").

There are "rate limits" to how much data and how many files you can transfer in any 24 hours period. If you are archiving data to Google Drive, it is much better to first compress folders that contain lots of small files (e.g. using [tar](/online-tutorials)) before transferring. If you have hit your rate limit, Globus should automatically resume the transfer during the next 24 hour period. If you click the "sync" checkbox in the Transfer Setting window on the Globus page, Globus should resume the transfer where it left off when it hit the limit.

In our testing, we have seen up to 10MB/s upload and 100MB/s download speeds.

### Managing Your Endpoint

To manage your endpoint, such as delete the endpoint, rename it, or share it with additional people (be aware, they will be able to access your Google Drive), go to [Manage Endpoint](https://app.globus.org/endpoints) on the Globus website.
