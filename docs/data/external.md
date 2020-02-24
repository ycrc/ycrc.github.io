# Serving Research Data Externally

If you need to serve research data externally (outside of Yale), it can be a challenge, since most Yale servers have internal IP addresses that are not externally accessible.  A common example is hosting tracks for the UCSC Genome Browser, which requires loading data onto an http server that is publically accessible.

The best way we have found to do this is to use ITS's [spinup](http://spinup.internal.yale.edu) service.  Create a "static website", giving it an appropriate website name.  The static website is just an S3 bucket with a webserver and a public IP and hostname.  

Then, use any S3 tool to upload your files to the static website.  The FAQ on the spinup FAQ for S3 buckets lists a number of suggested upload tools and explains how to use them, including the AWS CLI, CrossFTP, and Cyberduck.  

Note that there will be a modest cost for storing the data (a few cents per GB per month).

