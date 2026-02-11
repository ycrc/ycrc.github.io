# YCGA Data Permissions

Primary sequencing data produced by YCGA is only made accessible to the groups that submitted the data.

In order to improve the security of fastq sequence data on the Yale HPC system (McCleary) we will be tightening permissions on that data to restrict access to the group that submitted the samples.  We will do our best to allow access by the correct groups, but in some cases you may lose access when we make the change.

This change only impacts data in directories managed by YCGA; it does not impact sequencing data in your own directories.  

In addition, you will no longer be able to directly access or download data from the sequence data archive (/SAY/archive/YCGA-729009-YCGA-A2/archive/…).  To access archived data, you must use ycgaFastq or URLFetch, see below.

We will make this change on Oct 1, 2024.  After that date, if you discover that you no longer have access to your data, please contact research.computing@yale.edu.  Please provide the path to the data you wish to access, as well as a list of groups and/or users who you believe should have access.  YCRC and YCGA will review the request and restore access if approved.  Also, if you frequently require access to another group’s sequencing data, we recommend that you ask the group’s PI to add you to their group, which will give you access to all of their sequencing data.

You can check to see who is a member of your group by running 
/share/admins/bin/lman show groupname.  
To add users to a group, the PI should send an email to research.computing@yale.edu.  You can use this template:


Please add <netid> to my group, and also make them a member of the ycga group.
Illumina (not 10x) data:
This is data located here: /gpfs/ycga/sequencers/illumina
You can continue to access your illumina data using ycgaFastq and the url provided by YCGA or the original path to the data, exactly as before.

module load ycga-public
ycgaFastq fcb.ycga.yale.edu:3010/randomstring/sample_dir_001
or
ycgaFastq /gpfs/ycga/sequencers/illumina/sequencerC/runs/…/Project_Foo

If the fastq files are still on disk, ycgaFastq will simply make links.  If the data has been archived, it will be extracted from the archive and copied to your directory.
10x and Pacbio data:
You may continue to use wget or similar to download data using the url.  However, we recommend that you access this data using URLFetch:

module load ycga-public
URLFetch http://fcb.ycga.yale.edu:3010/randomstring/stagingdir

If the fastq files are still on disk, URLFetch will simply make links.  If the data has been archived, it will be automatically extracted from the archive and copied to your directory.

Please let us know if you have any questions or concerns about this change.

Sincerely,

Shrikant Mane
Director, YCGA


