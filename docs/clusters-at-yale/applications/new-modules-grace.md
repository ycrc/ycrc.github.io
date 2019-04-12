# New Module System

During the August 2019 Grace scheduled maintenance, we will be switching the default module collection. This upgrade will make the cluster more consistent with our other clusters' software environments and allow us to resolve software installation requests more quickly. The old software collection will be available for the time being (see below), but all new software installations will go into the new collection.

## Key Differences

### Module Names

The new module collection is built using a tool called "EasyBuild", which uses a system of "toolchains" to more transparently constrain software dependencies and compatibility. See [this page](/node/16575) for more information on EasyBuild and toolchains. As such, modules will no longer be prefixed with a category such as "Apps" or "Langs", but instead will have a suffix describing its toolchain (if applicable).

``` bash
# old:
module load Apps/Octave/4.2.1
# new: 
module load Octave/4.2.1-foss-2016b
```

You will need to update your scripts to load modules using their new names. Note that these are new installations of the same software (not redirects to the old installations), so please let us know if anything isn't working as expected. Any software you have compiled for yourself will likely need to be recompiled with the new modules.

### Python and R

With the growth of users on our clusters, installing and maintaining central versions of Python and R with all the requested packages has become extremely complicated and unsustainable. As such, our recommendation is now to install [a personal Python or R environment using conda](/node/14571) which will install the packages of your choosing into your directory. If you run into any difficulty with these environments, we are happy to help--just email us at hpc@yale.edu.

## To Try and/or Switch to the New Collection

To try the new collection and see if all the software you require is available (email us if anything is missing!), run the following command:

``` bash
source /apps/bin/try_new_modules.sh
```

This will switch your module collection (visible via "module avail") to the new one for that session. To revert, simply log out and log back in. To switch permanently, run `module save` after running the above command.

## To Use Old Software

To use any of the old software (after switching), run the following commands on the login node:

``` bash
module use /gpfs/loomis/apps/hpc.rhel6/Modules
module use /gpfs/loomis/apps/hpc.rhel7/Modules
module save
```

Then you should see all the old software if you run "module avail". To then remove the old software collection from your list, run:

``` bash
module unuse /gpfs/loomis/apps/hpc.rhel6/Modules
module unuse /gpfs/loomis/apps/hpc.rhel7/Modules
module save
```

We will be deprecating the old software at a TBD date, so we encourage you to contact us if anything is missing or not working for you in the new collection.