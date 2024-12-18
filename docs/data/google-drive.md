# Google Drive

Through Yale Google Apps for Education (EliApps), researchers have access to 5GB of storage with the option to purchase additional storage as needed. The Globus Google Drive connector allows you to create a Globus endpoint that allows you to use the Globus infrastructure to transfer data into your Google Drive account. As always, no sensitive data (e.g. ePHI, HIPAA) is allowed in Google Drive storage.

## EliApps

If your Yale email account is already an EliApps account (Gmail), then you are all set. If your Yale email is in Microsoft Office365, send an email to the [ITS helpdesk](mailto:helpdesk@yale.edu) requesting a "no-email EliApps account". Once it is created you can login to Google Drive using your EliApps account name, which will be of the form `netid@yale.edu`. The Globus connector is configured to only allow data to be uploaded into EliApps Google Drive accounts.

### Google Shared Drives (formerly Team Drive)

[Shared Drives](https://support.google.com/a/users/answer/9310246?hl=en&sjid=16812813776924550361-NA&visit_id=638216600368404114-927829563&ref_topic=9296420&rd=1) is an additional feature for EliApps that 
is available by request only (through Yale ITS). A Shared Drive is a Google Drive space that aims to solve most ownership and permissions issues present with traditional shared Google Drive folders. Once a 
Shared Drive is created, e.g. for a project or research group, any data placed in that Drive are owned by the drive and permissions (which accounts can own or access the data) can be easily managed from 
the Shared Drive interface by drive owners. With Shared Drive, you can be sure the data will stay with the research group as students and postdocs come and go. Although group members are initially provided 
with a default EliApps Storage quota, this can be increased as needed by reaching out through the [Yale ITS Google Shared 
page](https://yale.service-now.com/it?id=service_offering&sys_id=4f584dcd6fbb31007ee2abcf9f3ee40e). Aside from these quota limits, there are also [limits for Google Shared Drives](https://support.google.com/a/answer/7338880?hl=en) put in place by Google directly. Some are listed below.

!!! warning
     To keep file counts low (and for easier data retrieval) we *highly* recommended that you archive your data using zip or [tar](/resources/online-tutorials/#how-create-and-extract-a-tar-or-targz-archive).

| Limit type                                | Limit   |
|-------------------------------------------|---------|
| Number of files and folders               | 400,000 |
| Daily upload cap                          | 750 GiB |
| Max individual file size                  | 5 TiB   |
| Max number of nested folders              | 20      |


## Local File Access

You can upload and access your data using the web portal and sync data with your local machines via the Google File Stream software. For sync with your local machine, install [Drive for desktop](https://www.google.com/drive/download/). Authenticate with your EliApps account and you will see Google Drive mounted as an additional drive on your machine.

## Rclone

You can also transfer data using the command line utility [Rclone](/data/transfer/#rclone). Rclone can be used to transfer data to any Google Drive account.

## Globus Google Drive Connector

You can use Globus to transfer data to/from any EliApps Google Drive as well. See our [Globus](/data/globus) documentation for more information.



