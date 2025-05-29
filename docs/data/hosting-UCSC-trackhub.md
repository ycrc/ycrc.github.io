# Hosting a UCSC Custom Track Hub

The [UCSC Genome Browser](https://genome.ucsc.edu/) is a web-based tool for visualizing genomic data.
It supports the loading of custom track data, which are files containing genome-indexed data for visualization.
To host your own custom track data for public use, you can create a UCSC Custom Track Hub. 

This requires a few steps:  
1. Create a custom track hub directory on the cluster  
2. Create a static website on Yale Spinup to host the files publicly  
3. Upload the track hub files to the static website's storage (AWS S3)  
4. Connect the track hub to the UCSC Genome Browser  

!!! warning  
    Yale Spinup static sites are approved only for hosting of low-risk data.

## 1. Create a custom track hub directory on the cluster

The track hub directory is a directory on the cluster that contains the files defining the track hub and its component data files, as well as necessary metadata. The format of the track hub directory is expected to match the [UCSC Custom Track Hub format](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp.html#Setup). For example:
```
myHub
    ├── hg19
    │   ├── dnase.html
    │   ├── dnaseLiver.bigBed
    │   ├── dnaseLiver.bigWig
    │   ├── dnaseLung.bigBed
    │   ├── dnaseLung.bigWig
    │   ├── liverGenes.bigGenePred
    │   └── trackDb.txt
    ├── genomes.txt
    ├── hub.html
    └── hub.txt
```
For details on each of the UCSC Custom Track Hub files, see the UCSC documentation linked above.  


## 2. Create a static website on Yale Spinup to host the files publicly

Yale Spinup is a platform for hosting cloud computing resources on Amazon Web Services (AWS).
Among Spinup's offerings is a static website service, which allows you to host static data on AWS S3 and serve the data over the Internet via a custom domain. We will use this service to host the track hub files publicly.

1. Follow the instructions [here](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/4563009560/Spinup+Quick+Start+Guide) to create a Spinup Space if you do not already have one. You will require a COA code for cost charging. 
2. Follow the instructions [here](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/905969895/How+do+I+use+a+Spinup+static+website) to create a static website in your Spinup Space.

You should be able to access the static website at `<your-site-name>.yalepages.org/` or `<your-site-name>.yalespace.org/`, depending on the domain name you selected when setting up the static website.  
The test message on the website should read, "Hello, `<your-site-name>`.yalepages.org!"


## 3. Upload the track hub files to the static website's storage (AWS S3)

### 3.1 Create a user for the static website
1. On the Spinup dashboard, click on the static website you created.
2. Click the "New User" button under the "Users" section.
3. Enter a name for the user, leave the "Access Path" as default, select the "Admin" access level, and click "Generate User".
4. Copy the displayed `AccessKeyId` and `SecretAccessKey` to a secure location. 
5. Close the key details window and copy the `DistributionId` from the "Storage Details" section of the page to a secure location.

### 3.2 Upload the track hub files
5. In a cluster terminal session, run `module load awscli`
6. Run `aws configure --profile <your-site-url>` and input the saved AccessKeyId and SecretAccessKey. Accept default values for region and output format.
7. Run `export AWS_PROFILE=<your-site-url>` to set the configured profile for the current terminal session.
8. Run `aws s3 sync <path-to-track-hub-directory> s3://<your-site-url>/` to upload the track hub files to the static website's storage.
9. Run `aws cloudfront create-invalidation --distribution-id <your-distribution-id> --paths '/*'` to refresh the cache for the static website.


## 4. Connect the track hub to the UCSC Genome Browser

1. Browse to [https://genome.ucsc.edu/cgi-bin/hgHubConnect](https://genome.ucsc.edu/cgi-bin/hgHubConnect) and click the "Connected Hubs" tab.
2. Enter the URL `https://<your-site-url>/hub.txt` and click "Add Hub".
3. If successful, you will be shown the "Hub Connect Successful" page.
4. On the Hub Connect Successful page, click a link for a genome assembly to view your tracks in the UCSC Genome Browser. 
5. To share the track hub with others, you can provide them with a URL of the following format: `http://genome.ucsc.edu/cgi-bin/hgTracks?db=<assembly-name>&hubUrl=https://<your-site-url>/hub.txt`.  
For example, `http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&hubUrl=https://test-ucsc-trackhub.yalepages.org/hub.txt` will show the tracks for the hg19 assembly.

## 5. Updating the track hub

If you make changes to the track hub files on the cluster, you must upload the changes to the static website's storage (AWS S3):  
1. Run `module load awscli`  
2. Run `aws s3 sync <path-to-track-hub-directory> s3://<your-site-url>/` to upload the track hub files to the static website's storage.

You may need to wait a few minutes for the changes to propagate. 

## Finished!

You should now be able to view your tracks in the UCSC Genome Browser.

If you have any questions, please contact YCRC Research Support at mailto:research.computing@yale.edu.