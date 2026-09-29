# Share Data Outside Yale

## Share data using Microsoft OneDrive
Yale ITS's recommended way to send other people large files is by
using Microsoft OneDrive.  See [details](https://yale.service-now.com/it?id=support_article&sys_id=eeece8c91bfb6010806141d8cd4bcb58).

## Public Website

Researchers frequently ask how they can set up a public website to share data or provide a web-based application.  The easiest way to do this is by using Yale ITS's spinup service.  

First get an account on [Spinup](http://spinup.internal.yale.edu).
!!! info
    When getting your account on Spinup, you will need to provide a charging account (aka COA). 
 

### Static Website

You can use a static website with a public address to serve data publicly to collaborators or services that need to see the data via http. A common example of this is hosting tracks for the UCSC Genome Browser. 
Note that this only serves static files.  If you wish to host a dynamic web application, see below.

ITS's spinup service makes creating a static website easy and inexpensive.  

Follow their [instructions on creating a static website](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/905969895/How+do+I+use+a+Spinup+static+website), giving it an appropriate website name.  Make sure to save the access key and secret key, since you'll need them to connect to the website.  The static website will incur a small charge per month of a few cents per GB stored or downloaded.

Then use an [S3 transfer tool](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/829292599/How+do+I+use+a+Spinup+S3+bucket) like Cyberduck, AWS CLI, or CrossFTP to connect to the website and transfer your files.  The spinup page for your static website provides a link to a Cyberduck config file. 
That is the probably the easiest way to connect. 

#### UCSC Hub

To set up the UCSC Hub, follow their [directions](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp) to set up the appropriate file heirarchy on
your static website, using the transfer tool.

### Web-based Application
If your web application goes beyond simply serving static data, the best solution is to create a spinup virtual machine (VM), set up your web application on the VM, then 
follow the spinup [instructions on requesting public access to a web server](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/643170314/Requesting+Public+Access+to+a+Spinup+Hosted+Web+Application+or+Website)

!!! info
    Running a VM 24x7 can incur significant costs on spinup, depending on the size of the VM.  

## Private Share Using Globus

[Globus](/data/globus) can be used to shared data hosts on one of the clusters privately with a specific person or group of people.

1. From the [file manager interface](https://app.globus.org/file-manager) enter the name of the endpoint you would like to share from in the collection field (e.g. "Yale CRC Grace")
1. Click the Share button on the right
1. Click on "Add Guest Collection"
1. Next to Path, click "Browse" to find and select the directory you want to share
1. Add other details as desired and click on "Create Share"
1. Click on "Add Permissions -- Share With"
1. Under "Username or Email" enter the e-mail address of the person that you want to share the data with, then click on "Save", then click on "Add Permission"
1. Do not select "write" unless you want the person you are sharing the data with to be able to write to your storage on the cluster.

For more information, please see the [official Globus Documentation](https://docs.globus.org/how-to).

