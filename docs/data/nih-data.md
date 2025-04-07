# NIH Controlled-Access Data and Repositories

Effective January 25, 2025, adherence to the updated security standards in the [NIH Security Best Practices for Users of Controlled-Access Data](https://sharing.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf) is included in new or renewed Data Use Certifications or similar agreements.
This means that such data must be stored and computed in a NIST 800-171 compliant environment.
YCRC's new [Hopper cluster](/clusters/hopper) as well as a secure version of SpinUp is expected be available and HIPAA/NIST 800-171 compliant this summer. 

In the meantime, the NIH is allowing environments with Plans of Action and Milestones (POAMs) to mitigate security risks to be considered compliant.
As of April 4th, 2025, Yale has completed appropriate documentation for McCleary.
[McCleary](/clusters/mccleary) is now an approved location of specifically NIH Controlled-Access Data and Repositories, with the following conditions.
McCleary, under the following conditions, is the ONLY shared computing environment at Yale suitable for NIH Controlled-Access Data and Repositories.

!!! info
	A list of NIH Controlled-Access Data and Repositories can be found on the [NIH Website](https://sharing.nih.gov/accessing-data/NIH-security-best-practices).


## Special Conditions to Ensure Compliance

### Data Storage

To ensure compliance, McCleary now has a special storage space, located at `/vast/palmer/nih`, for storing Controlled-Access Data.
All NIH Controlled-Access Data and Repositories and derivatives cannot be storage in another location on McCleary or any other YCRC cluster.
Approved projects will be granted a directory and quota under `/vast/palmer/nih`. In order to facilitate the affected work and due to the short term solution on McCleary, storage quota within reason will be granted free of charge.

### Data Transfer

As McCleary is the only approved computing environment at this time for NIH Controlled-Access Data, you may not transferred the data off the cluster to any other system including personal computers (with the exception of Hopper when it is available).


### Transition to Hopper

All NIH Controlled-Access projects will need to be transferred off of McCleary as soon as Hopper is in production (expected summer 2025).
The YCRC will facilitate the transfer of all data to Hopper and then projects and all associated data will be purged from McCleary.
Hopper, as a NIST 800-171/HIPAA compliant environment, is more restricted that McCleary, so researchers should be prepared for differences in the user experience.
On such restriction is completion of a virtual training program (a few hours in duration) that will required for access to Hopper.


## Request Project

To request a special project for storing and computing against NIH Controlled-Access Data and Repositories, please submit the following form.

[Request Project Access on McCleary](https://forms.gle/42Uc4YwRPNwHKq8Y8){ .md-button }