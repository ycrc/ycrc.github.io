# ATLAS Computing Environment


Software for the [ATLAS experiment](https://home.web.cern.ch/science/experiments/atlas) is available on our clusters via [CVMFS](https://cernvm.cern.ch/fs/).
The ATLAS user interface can be set up by adding these lines to your `.bashrc` file:

```sh
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
alias setupATLAS='source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh'
```

Then simply running `setupATLAS -h` will show all the options available:

```sh
[testuser@login2.grace ~]$ setupATLAS -h

Usage: atlasLocalSetup.sh [options]
       or setupATLAS [options]

    This sets up the ATLAS environment for a cluster user

    You need to set the environment variable ATLAS_LOCAL_ROOT_BASE first.

    Options (to override defaults) are:
     -3                           Use python3 in tools (if available)
     -2				  Use python/python2 in tools (if available)
     -h  --help                   Print this help message
     -q  --quiet                  Print no output
     -p  --noLocalPostSetup       Skip running local/site post-setup script
     -r  --relocateCvmfs          Use relocated cvmfs
     -t  --test=STRING            Comma delimited strings for dev/test flags
     -c  --container=name         setupATLAS in a container
                                   Type setupATLAS -c -h for help

Comma delimited arguments to -t/--test option are:
 cmtSL6-dev	Use dev version of cmtSL6
 devatlr	Use CERN FRONTIER servlet for developers
 postRel-dev	Uses a dev version of the post release setup for ATLAS releases
 tokens  	Use tokens for validation instead of X509 (where available)

```
We recommend referring to the [ATLAS Canada TWiki](https://twiki.atlas-canada.ca/bin/view/AtlasCanada/ComputingPage) for more information and detailed start-up guides. 
