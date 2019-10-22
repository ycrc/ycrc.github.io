# Google Drive

Through Yale Google Apps for Education (Eliapps), researchers have free, unlimited Google Drive storage. The Globus Google Drive connector allows you to create a Globus endpoint that allows you to use the Globus infrastructure to transfer data into your Google Drive account. As always, no sensitive data (e.g. ePHI, HIPAA) is allowed in Google Drive storage.

## Eliapps

If your Yale email account is already an Eliapps account (Gmail), then you are all set. If your Yale email is in Microsoft Office365, you can request a "no-email Eliapps" account. To do this, send an email to the [ITS helpdesk](mailto:helpdesk@yale.edu) to requesting a "no-email Eliapps account". Once it is created, you should be able to login to Google Drive using your Eliapps account name, which will be `<netid>@yale.edu`. The Globus connector is configured to only allow data to be uploaded into Eliapps Google Drive accounts.

### Google Shared Drives (formerly Team Drive)

[Shared Drives](https://gsuite.google.com/learning-center/products/drive/get-started-team-drive/#!/) is an additional feature on Eliapps that is available by request only (at the moment). A Shared Drive is a Google Drive space that solves a lot of ownership and permissions issues present with traditional shared Google Drive folder. Once you create a Shared Drive, e.g. for a project or research group, any data placed in that Drive are owned by the drive and the permission (which accounts can own or access the data) can be easily managed from the Shared Drive interface by drive owners. With Shared Drive, you can be sure the data will stay with research group as students and postdocs come and go. To request Shared Drive, first make sure you have an Eliapps account (see above) and then send a request to research.computing@yale.edu and we will work with ITS on your behalf to enable the feature.

!!!warning
    Google Shared Drives have a file count limit of 400,000 files. Therefore, it is highly recommended that you compress you compress portions of your data, using zip or [tar](/online-tutorials), to keep the file count low and for ease of storage and retrieval.

### Local File Access

You can upload and access your data using the web portal and sync data with your local machines via the Google File Stream software. For sync with your local machine, install [Google File Stream](https://www.google.com/drive/download/). Select the Download button on the left side under “Business” and authenticate with your Eliapps account. You will see Google Drive mounted as an additional drive on your machine.

### Rclone

You can also transfer data using the command line utility [Rclone](https://rclone.org/drive/). Rclone can be used to transfer data to any Google Drive account.

## Globus Google Drive Connector

The Globus connector is configured to only allow data to be uploaded into Eliapps (Yale's GSuite for Education) Google Drive accounts. If you don't have an Eliapps account, request one as described above.

### Set Up Your Endpoint

1. To set up your Globus Google Drive endpoint, click on the following link: [Setup Globus Google Drive Endpoint](https://collections.globus.org/systems?client_id=4c133fd7-3dd6-4dee-8726-b3111a3429a5)
1. Log into Globus, if needed.
1. The first time you create an endpoint, you will be presented with a permissions approval page. If you are ok with the Connector manipulating your files through Globus (which is required), click the Allow button.
1. The next page should say "Create a shared endpoint". Click on "Yale Google Drive Gateway (Google Drive)".
1. Again, the first time you create an endpoint, you will be asked to register your Google Eliapps account with Globus. Put in your Eliapps account (either your email address if you are an Eliapps user, or `<netid>@yale.edu` if you are no-email Eliapps user) and submit the form. You will then be asked on a series of Google pages to select or login into your Eliapps account and then approve Globus to write to your Google Drive.
1. You will then be redirected back to Globus to fill out a form to "Create a Shared Endpoint". The only required field are (all others can be left blank):
    * "Credentials" - should be prefilled with your yale account
    * "Endpoint Display Name" - this is the name of your endpoint and the name you will use to search for the endpoint in the Globus transfer interface. We recommend including your netid or name in the endpoint so you can uniquely identify it, such as "<netid> Google Drive"
1. After filling out the form, click the "Create Endpoint" button.
1. If your endpoint was successfully created, you should see a page with a green checkmark and three links. Click on the middle link to start transferring data to or from your Google Drive!

### Using Your Endpoint

On the [Globus Transfer](https://www.globus.org/app/transfer) page, select an endpoint for each side of your transfer. To transfer to or from your Google Drive, simply search in the Endpoint field for the name of the Endpoint you created above (e.g. "<netid> Google Drive").

There are "rate limits" to how much data and how many files you can transfer in any 24 hours period. If you are archiving data to Google Drive, it is much better to first compress folders that contain lots of small files (e.g. using [tar](/online-tutorials)) before transferring. If you have hit your rate limit, Globus should automatically resume the transfer during the next 24 hour period. If you click the "sync" checkbox in the Transfer Setting window on the Globus page, Globus should resume the transfer where it left off when it hit the limit.

In our testing, we have seen up to 10MB/s upload and 100MB/s download speeds.

### Managing Your Endpoint

To manage your endpoint, such as delete the endpoint, rename it, or share it with additional people (be aware, they will be able to access your Google Drive), go to [Manage Endpoint](https://www.globus.org/app/endpoints) on the Globus website.