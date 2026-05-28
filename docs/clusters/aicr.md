# AICR

[AICR](https://www.mass.gov/news/governor-healey-advances-states-ai-leadership-with-major-investments-in-massachusetts-ai-hub) is a multi-institution AI-focused computing cluster at MGHPCC that will be available to Yale researchers later this year.
The system is designed to accelerate AI innovation by providing the compute and data capacity essential for cutting-edge development.
This effort is a partnership between the Massachusetts Commonwealth and MGHPCC’s six member universities—Boston University, Harvard University, MIT, Northeastern University, the University of Massachusetts, and Yale University.

The cluster initially contains 248 B200 GPUs and 152 RTX Pro 6000 Blackwell GPUs for AI and AI-enabled research. 

## Access the Cluster

AICR will be available in Spring 2026.
AICR availability and information on how to request access will be announced to the YCRC user mailing list and the YCRC Bulldog newsletter.

Later in 2026 access to AICR will be granted via an internal Yale proposal process (details to be announced).
All active projects will be expected to submit to and be approved through that process to continue to have AICR access.

### Certificate-signed SSH Keys

AICR uses certificate-signed SSH keys that are generated for you and put into your account. To get these keys you:

- Log into http://ood.aicr.ai with your CAS credentials
- Open the File Browser and download the aicr\_keys.zip file 

To install these keys follow these steps:

```sh
# copy keys to local $HOME/.ssh directory
cp aicr_keys/id_ed25519_aicr* $HOME/.ssh/

# fix permissions on private key
cd $HOME/.ssh/
chmod 600 id_ed25519_aicr

# To change passphrase (initial passphrase is in aicr_keys/.passphrase):
ssh-keygen -p -f $HOME/.ssh/id_ed25519_aicr

# Then (needs passphrase):
ssh-add id_ed25519_aicr

#To log in:
ssh username@login.aicr.ai
```
Your AICR username is your netid followed by `_yale`, for example: `abc123_yale`.⠀


## Installed Applications

A large number of software and applications are installed on our clusters, including AICR.
AICR software will be made available to researchers via [software modules](/applications/modules/). 

During Early Access researchers you will need to add this line to your `$HOME/.bashrc` file to get access to our software modules:

```
export MODULEPATH=/apps/yale/modules/2026.1:/apps/yale/modules/2024a:/apps/yale/modules/system:$MODULEPATH
```

This will eventually be replaced by a StdEnv, but that is still in progress.

If you need a specific application that is not present, let us know and we can install it for you.

## Partitions and Hardware

AICR initially contains 248 B200 GPUs and 152 RTX Pro 6000 Blackwell GPUs, grouped into [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. 
Currently, there are five partitions:

- `cpu`: a small CPU-only partition for jobs which do not require GPU cars
- `rtx-devel` and `b200-devel`: interactive access to GPUs, comprised of ~10% of the available cards
- `rtx-batch` and `b200-batch`: large, batch-job-only partitions 

All nodes feature the same AMD 9575F CPUs with 128 cores (across two sockets). 
The CPU nodes offer 1TB of RAM, while the GPU nodes all have 2.2TB. 

Note, the default job parameters are slightly different than YCRC clusters. 
The most notable differences are the default time-limit of 15 minutes and the default memory allocation of 1GB.  

## Storage

AICR has access to an all-flash, NFS filesystem similar to the Roberts filesystem on Bouchet and the Palmer filesystem on Grace and McCleary.


|Partition       | Root Directory            | Storage                                 | File Count | Backups | Snapshots | Notes |
|----------------|---------------------------|-----------------------------------------|------------|---------|-----------|-------|
| home           | TBD | 100GiB/user                             | 500,000    | No     | 7 days  |       |
| work        | TBD     | TBD | TBD | No      | 7 days  |       |
| scratch        | TBD    | 10TiB/user                             | 15,000,000 | No      | No        |       |

