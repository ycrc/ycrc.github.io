# Share Data Outside Yale

## Public Website

You can use a static website with a public address to serve data publicly to collaborators or services that need to see the data via http. A common example of this is hosting tracks for the UCSC Genome Browser. 

ITS's spinup service makes this easy and inexpensive.  

To set one up, first get an account on ITS's [Spinup](http://spinup.internal.yale.edu) service. 
After that, follow their [instructions on creating a static website](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/905969895/How+do+I+use+a+Spinup+static+website), giving it an appropriate website name.  Make sure to save the access key and secret key, since you'll need them to connect to the website. 

!!! info
    When getting your account on Spinup, you will need to provide a charging account (aka COA).  The static website will incur a small charge per month of a few cents per GB stored or downloaded.

Then use an [S3 transfer tool](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/829292599/How+do+I+use+a+Spinup+S3+bucket) like Cyberduck, AWS CLI, or CrossFTP to connect to the website and transfer your files.  The spinup page for your static website provides a link to a Cyberduck config file. 
That is the probably the easiest way to connect. 

### UCSC Hub

To set up the UCSC Hub, follow their [directions](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp) to set up the appropriate file heirarchy on
your static website, using the transfer tool.

## Private Share Using Globus

[Globus](/data/globus) can be used to shared data hosts on one of the clsuters privately with a specific person or group of people.

1. From the [file manager interface](https://app.globus.org/file-manager) enter the name of the endpoint you would like to share from in the collection field (e.g. yale#grace)
1. Click the Share button on the right
1. Click on "Add a Shared Endpoint"
1. Next to Path, click "Browse" to find and select the directory you want to share
1. Add other details as desired and click on "Create Share"
1. Click on "Add Permissions -- Share With"
1. Under "Username or Email" enter the e-mail address of the person that you want to share the data with, then click on "Save", then click on "Add Permission"
1. Do not select "write" unless you want the person you are sharing the data with to be able to write to your storage on the cluster.

For more information, please see the [official Globus Documentation](https://docs.globus.org/how-to).


