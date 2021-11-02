# Data Storage Options

## Google Drive via EliApps

**Capacity: Unlimited. Cost: Free - 5TiB max file size  
No sensitive data (e.g. ePHI, HIPAA)  
Can be mounted on [your local machine](https://www.google.com/drive/download/) and transferred to via [Globus Google Drive Connector](/clusters-at-yale/data/globus)**

Google Drive is a cloud service for file storage, document editing and sharing. All members of the Yale community with an EliApps (Google Workspace for Education) account have storage at no cost in the associated Google Drive account. Moreover, EliApps users can request Shared Drives, which are shared spaces where all files are group-owned. For more information on Google Drive through EliApps, see our [Google Drive documentation](/data/google-drive).

## Storage @ Yale

**Capacity: As requested. Cost: See below  
No sensitive data (e.g. ePHI, HIPAA) for cluster mounts  
Can be mounted on the cluster or computers on campus (but not both)**

Storage @ Yale (S@Y) is a central storage service provided by ITS. S@Y shares can either be accessible on campus computers or the clusters, but not both. All prices are charged monthly for storage used at that time.

| Type        | Use                                                                           | Price           |
|-------------|-------------------------------------------------------------------------------|-----------------|
|Object Tier  |Good for staging data between cloud and clusters                               |$12/TiB/month    |
|Active Tier  |Daily use, still copy to cluster before using in jobs                          |$10.78/TiB/month |
|Archive Tier |Long term storage, low access. [Make sure to properly archive](/data/archive/) |$3.60/TiB/month  |

For most up to date pricing information, see the [ITS Data Rates](https://yale.service-now.com/it?id=rates_charges&service_group=e0502b7a1b3d3704f61dfeeccd4bcbab&service_offering=f4688dcd6fbb31007ee2abcf9f3ee400).

To request a share, press the “Request this Service” button in the right sidebar on the [Storage@Yale website](https://yale.service-now.com/it?id=service_offering&sys_id=f4688dcd6fbb31007ee2abcf9f3ee400). If you would like to request a share that is mounted on the clusters, **specify in your request that the share be mounted from the HPC clusters**. If you elect to use archive tier storage, be cognizant of [its performance characteristics](/data/archive).

!!! note "Cluster I/O Performance"
    Since cluster-mounted S@Y shares do *not* provide sufficient performance for use in jobs, they are not mounted on our compute or login nodes. To access S@Y on the clusters, connect to one of the transfer nodes to [stage the data](/clusters-at-yale/data/staging) to [Project](/clusters-at-yale/data/#project) or [Scratch60](/clusters-at-yale/data/#60-day-scratch) before running jobs.


## Box at Yale

**Capacity: 50GiB per user. Cost: Free. 15 GiB max file size.  
Sensitive data (e.g. ePHI, HIPAA) only in Secure Box  
Can be mounted on your local machine and transferred with [`rclone`](https://rclone.org/)**

All members of the Yale community have access to a share at Box at Yale. Box is another cloud-based file sharing and storage service. You can upload and access your data using the web portal and sync data with your local machines via Box Sync.

To access, navigate to [yale.box.com](http://yale.box.com) and login with your yale.edu account.

For sync with your local machine, install [Box Sync](https://sites.box.com/sync4/) and authenticate with your yale.edu account.

[For more information about Box at Yale, see the ITS website.](https://yale.service-now.com/it?id=service_offering&sys_id=ff584dcd6fbb31007ee2abcf9f3ee4ee)
