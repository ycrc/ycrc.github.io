# New Module System

During the August 2019 Grace scheduled maintenance, we switched the default module collection. 
This upgrade makes the cluster more consistent with our other clusters' software environments and 
allows us to resolve software installation requests more quickly. 
The old software collection is still available for the time being (see below), but all new software 
installations will go into the new collection.

## Key Differences

### Module Names

The new module collection is built using a tool called "EasyBuild", which uses a system of "toolchains" 
to more transparently constrain software dependencies and compatibility. 
See [this page](/clusters-at-yale/applications/easybuild) for more information on EasyBuild and toolchains. 
As such, modules are no longer prefixed with a category such as "Apps" or "Langs", but instead have a 
suffix describing its toolchain (if applicable).

``` bash
# old:
module load Apps/Octave/4.2.1
# new: 
module load Octave/4.2.1-foss-2016b
```

You will need to update your scripts to load modules using their new names. 
Note that these are new installations of the same software (not redirects to the old installations), so please let us know if anything isn't working as expected. 
Any software you have compiled for yourself will likely need to be recompiled with the new modules.

### Python and R

With the growth of users on our clusters, installing and maintaining central versions of Python and R with all the requested packages has become extremely complicated and unsustainable. As such, our recommendation is now to install [a personal Python or R environment using conda](/clusters-at-yale/guides/conda) which will install the packages of your choosing into your directory. If you run into any difficulty with these environments, we are happy to help--just email us at hpc@yale.edu.

## To Use Old Software

To use any of the old software, run the following commands:

``` bash
module use /gpfs/loomis/apps/hpc.rhel6/Modules
module use /gpfs/loomis/apps/hpc.rhel7/Modules
module save
```

Then you should see all the old software if you run "module avail". 
To then remove the old software collection from your list, run:

``` bash
module unuse /gpfs/loomis/apps/hpc.rhel6/Modules
module unuse /gpfs/loomis/apps/hpc.rhel7/Modules
module save
```

We will be deprecating the old software at a TBD date, so we encourage you to contact us if anything is missing or not working for you in the new collection.


## Lmod Warning

Some users have experienced warnings at login due to the module change impacting their default module 
environment. 
This warning looks like:

```sh
Last login: Thu Aug 29 14:53:22 EDT 2019 on pts/61
Lmod Warning:  One or more modules in your default collection have changed: "StdEnv".
To see the contents of this collection execute:
  $ module describe default
To rebuild the collection, do a module reset, then load the modules you wish, then execute:
  $ module save default
If you no longer want this module collection execute:
  $ rm ~/.lmod.d/default

For more information execute 'module help' or see http://lmod.readthedocs.org/
No change in modules loaded.

```

To resolve this warning, you will need to save a new default module environment. 
Load all the modules from the new module list that you wish to have loaded at login, for example:

```sh
module load R
module load dSQ

```

Then save that module environment:

```sh
module save
```

Then when you log out and log back in the warning should be gone.
