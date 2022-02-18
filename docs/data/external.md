# Serving Research Data Externally

You can use a static website with a public address to serve data publicly to collaborators or services that need to see the data via http. A common example of this is hosting tracks for the UCSC Genome Browser. 

ITS's spinup service makes this easy and inexpensive.  

To set one up, first get an account on ITS's [Spinup](http://spinup.internal.yale.edu) service. 
After that, follow their [instructions on creating a static website](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/905969895/How+do+I+use+a+Spinup+static+website), giving it an appropriate website name.  Make sure to save the access key and secret key, since you'll need them to connect to the website.   

Then use an [S3 transfer tool](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/829292599/How+do+I+use+a+Spinup+S3+bucket) like Cyberduck, AWS CLI, or CrossFTP to connect to the website and transfer your files.  The spinup page for your static website provides a link to a Cyberduck config file. 
That is the probably the easiest way to connect. 

To set up the UCSC Hub, follow their [directions](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp) to set up the appropriate file heirarchy on
your static website, using the transfer tool.

!!! info
    When getting your account on Spinup, you will need to provide a charging account (aka COA).  The static website will incur a small charge per month of a few cents per GB stored or downloaded.


