=== "Google Drive"
    
    The example below is a screen dump when setting up `rclone` for Google Drive.
    
    ```bash
    [pl543@c03n06 ~]$ rclone config
    No remotes found - make a new one
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    name> remote
    Type of storage to configure.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value
     1 / 1Fichier
       \ "fichier"
     2 / Alias for an existing remote
       \ "alias"
    [...]
    15 / Google Drive
       \ "drive"
    [...]
    42 / seafile
       \ "seafile"
    Storage> 15
    ** See help for drive backend at: https://rclone.org/drive/ **
    
    Google Application Client Id
    Setting your own is recommended.
    See https://rclone.org/drive/#making-your-own-client-id for how to create your own.
    If you leave this blank, it will use an internal key which is low performance.
    Enter a string value. Press Enter for the default ("").
    client_id> 
    OAuth Client Secret
    Leave blank normally.
    Enter a string value. Press Enter for the default ("").
    client_secret> 
    Scope that rclone should use when requesting access from drive.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value
     1 / Full access all files, excluding Application Data Folder.
       \ "drive"
     2 / Read-only access to file metadata and file contents.
       \ "drive.readonly"
       / Access to files created by rclone only.
     3 | These are visible in the drive website.
       | File authorization is revoked when the user deauthorizes the app.
       \ "drive.file"
       / Allows read and write access to the Application Data folder.
     4 | This is not visible in the drive website.
       \ "drive.appfolder"
       / Allows read-only access to file metadata but
     5 | does not allow any access to read or download file content.
       \ "drive.metadata.readonly"
    scope> 1
    ID of the root folder
    Leave blank normally.
    
    Fill in to access "Computers" folders (see docs), or for rclone to use
    a non root folder as its starting point.
    
    Enter a string value. Press Enter for the default ("").
    root_folder_id> 
    Service Account Credentials JSON file path 
    Leave blank normally.
    Needed only if you want use SA instead of interactive login.
    
    Leading `~` will be expanded in the file name as will environment variables such as `${RCLONE_CONFIG_DIR}`.
    
    Enter a string value. Press Enter for the default ("").
    service_account_file> 
    Edit advanced config? (y/n)
    y) Yes
    n) No (default)
    y/n> n
    Remote config
    Use auto config?
     * Say Y if not sure
     * Say N if you are working on a remote or headless machine
    y) Yes (default)
    n) No
    y/n> y
    If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth?state=6glRr_mpEORxHevlOaaYyw
    Log in and authorize rclone for access
    Waiting for code...
    Got code
    Configure this as a Shared Drive (Team Drive)?
    y) Yes
    n) No (default)
    y/n> n
    --------------------
    [remote]
    type = drive
    scope = drive
    token = {"access_token":"ya29.A0ArdaM-mBYFKBE2gieODvdANCZRV6Y8QHhQF-lY74E9fr1HTLOwwLRuoQQbO9P-Jdip62YYhqXfcuWT0KLKGdhUb9M8g2Z4XEQqoNLwZyA-FA2AAYYBqB","token_type":"Bearer","refresh_token":"1//0dDu3r6KVakgYIARAAGA0NwF-L9IrWIuG7_f44x-uLR2vvBocf4q-KnQVhlkm18TO2Fn0GjJp-cArWfj5kY84","expiry":"2021-02-25T17:28:18.629507046-05
    :00"}
    --------------------
    y) Yes this is OK (default)
    e) Edit this remote
    d) Delete this remote
    y/e/d> y
    Current remotes:
    
    Name                 Type
    ====                 ====
    remote               drive
    
    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q
    ```

=== "OneDrive"
    
    The example below is a screen dump when setting up `rclone` for Microsoft OneDrive.  This example was done inside a remote desktop in OOD, so rclone was able
    to start the browser to authenticate.  If you run this on a normal command line, you'll need to say 'N' at that step.
    
    ```bash
    [rdb9@r811u30n01.milgram ~]$ rclone config
    2024/08/06 11:09:57 NOTICE: Config file "/home/rdb9/.config/rclone/rclone.conf" not found - using defaults
    No remotes found, make a new one?
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n

    Enter name for new remote.
    name> yaleonedrive

    Option Storage.
    Type of storage to configure.
    Choose a number from below, or type in your own value.
     1 / 1Fichier
       \ (fichier)
     2 / Akamai NetStorage
       \ (netstorage)
    ...
    30 / Microsoft Azure Blob Storage
       \ (azureblob)
    31 / Microsoft OneDrive
       \ (onedrive)
    32 / OpenDrive
       \ (opendrive)
    ...
    Storage> 31

    Option client_id.
    OAuth Client Id.
    Leave blank normally.
    Enter a value. Press Enter to leave empty.
    client_id> 

    Option client_secret.
    OAuth Client Secret.
    Leave blank normally.
    Enter a value. Press Enter to leave empty.
    client_secret> 

    Option region.
    Choose national cloud region for OneDrive.
    Choose a number from below, or type in your own string value.
    Press Enter for the default (global).
     1 / Microsoft Cloud Global
       \ (global)
     2 / Microsoft Cloud for US Government
       \ (us)
     3 / Microsoft Cloud Germany
       \ (de)
     4 / Azure and Office 365 operated by Vnet Group in China
       \ (cn)
    region> 

    Edit advanced config?
    y) Yes
    n) No (default)
    y/n> 

    Use web browser to automatically authenticate rclone with remote?
     * Say Y if the machine running rclone has a web browser you can use
     * Say N if running rclone on a (remote) machine without web browser access
    If not sure try Y. If Y failed, try N.

    y) Yes (default)
    n) No
    y/n> y

    2024/08/06 11:12:43 NOTICE: If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth?state=Xt0h7NYaFt1F6ogeDRC0iQ
    2024/08/06 11:12:43 NOTICE: Log in and authorize rclone for access
    2024/08/06 11:12:43 NOTICE: Waiting for code...
    2024/08/06 11:13:45 NOTICE: Got code
    Option config_type.
    Type of connection
    Choose a number from below, or type in an existing string value.

    [ choose defaults from now on]

    Keep this "yaleonedrive" remote?
    y) Yes this is OK (default)
    e) Edit this remote
    d) Delete this remote
    y/e/d> 

    Current remotes:

    Name                 Type
    ====                 ====
    yaleonedrive         onedrive

    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q

    ```

=== "Box"
    
    The example below is a screen dump when setting up `rclone` for Yale Box.

    ```bash
    [pl543@c14n07 ~]$ rclone config
    No remotes found - make a new one
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    name> remote
    Type of storage to configure.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value
     1 / 1Fichier
       \ "fichier"
    [...]
     6 / Box
       \ "box"
    [...]
    Storage> box
    ** See help for box backend at: https://rclone.org/box/ **
    
    Box App Client Id.
    Leave blank normally.
    Enter a string value. Press Enter for the default ("").
    client_id> 
    Box App Client Secret
    Leave blank normally.
    Enter a string value. Press Enter for the default ("").
    client_secret> 
    Edit advanced config? (y/n)
    y) Yes
    n) No
    y/n> n
    Remote config
    Use auto config?
     * Say Y if not sure
     * Say N if you are working on a remote or headless machine
    y) Yes
    n) No
    y/n> y
    If your browser does not open automatically go to the following link: http://127.0.0.1:53682/auth
    Log in and authorize rclone for access
    Waiting for code...
    Got code
    --------------------
    [remote]
    type = box
    token = {"access_token":"PjIXHUZ34VQSmeUZ9r6bhc9ux44KMU0e","token_type":"bearer","refresh_token":"VumWPWP5Nd0M2C1GyfgfJL51zUeWPPVLc6VC6lBQduEPsQ9a6ibSor2dvHmyZ6B8","expiry":"2019-10-21T11:00:36.839586736-04:00"}
    --------------------
    y) Yes this is OK
    e) Edit this remote
    d) Delete this remote
    y/e/d> y
    Current remotes:
    
    Name                 Type
    ====                 ====
    remote               box
    
    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q
    ```
    
=== "S3"

    The example below is a screen dump when setting up `rclone` for an S3 provider such as aws.

    ```bash

    [rdb9@login1.mccleary ~]$ rclone config
    Enter configuration password:
    password:
    Current remotes:

    Name                 Type
    ====                 ====

    [...]

    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> n
	```bash

    Enter name for new remote.
    name> remote

    Option Storage.
    Type of storage to configure.
    Choose a number from below, or type in your own value.

    [...]

     5 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, China Mobile, Cloudflare, ArvanCloud, DigitalOcean, Dreamhost, Huawei OBS, IBM COS, IDrive e2, IONOS Cloud, Liara, Lyve Cloud, Minio, Netease, RackCorp, Scaleway, SeaweedFS, StackPath, Storj, Tencent COS, Qiniu and Wasabi
       \ (s3)
    [...]
    Storage> 5

    Option provider.
    Choose your S3 provider.
    Choose a number from below, or type in your own value.
    Press Enter to leave empty.
     1 / Amazon Web Services (AWS) S3
       \ (AWS)
    [...]
    provider> 1

    Option env_auth.
    Get AWS credentials from runtime (environment variables or EC2/ECS meta data if no env vars).
    Only applies if access_key_id and secret_access_key is blank.
    Choose a number from below, or type in your own boolean value (true or false).
    Press Enter for the default (false).
     1 / Enter AWS credentials in the next step.
       \ (false)
     2 / Get AWS credentials from the environment (env vars or IAM).
       \ (true)
    env_auth> 

    Option access_key_id.
    AWS Access Key ID.
    Leave blank for anonymous access or runtime credentials.
    Enter a value. Press Enter to leave empty.
    access_key_id> ***************

    Option secret_access_key.
    AWS Secret Access Key (password).
    Leave blank for anonymous access or runtime credentials.
    Enter a value. Press Enter to leave empty.
    secret_access_key> *************

    Option region.
    Region to connect to.
    Choose a number from below, or type in your own value.
    Press Enter to leave empty.
       / The default endpoint - a good choice if you are unsure.
     1 | US Region, Northern Virginia, or Pacific Northwest.
       | Leave location constraint empty.
       \ (us-east-1)
       / US East (Ohio) Region.
    [...]

    [take defaults for all remaining questions

    Edit advanced config?
    y) Yes
    n) No (default)
    y/n> n

    Configuration complete.
    Options:
    - type: s3
    - provider: AWS
    - access_key_id: ***************
    - secret_access_key: ****************
    - region: us-east-1
    ```