# Serving Research Data Externally

You can use a static website to serve data publicly to collaborators or services that need to see the data via http. A common example of this is hosting tracks for the UCSC Genome Browser. 

To set one up, first get an account on ITS's [Spinup](http://spinup.internal.yale.edu) service. After that, follow their [instructions on creating a static website](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/905969895/How+do+I+use+a+Spinup+static+website), giving it an appropriate website name. Then use an [S3 transfer tool](https://yaleits.atlassian.net/wiki/spaces/spinup/pages/829292599/How+do+I+use+a+Spinup+S3+bucket) like AWS CLI, CrossFTP, or Cyberduck to transfer your files.

!!! info
    There will be a cost for storing the data (a few cents per GB per month), which you can use Yale charging instructions to pay for.
