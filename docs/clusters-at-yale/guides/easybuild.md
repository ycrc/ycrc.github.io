# EasyBuild

The YCRC uses a framework called [EasyBuild](https://easybuild.readthedocs.io/en/latest/) to build and install the software you access via the [module system](https://docs.ycrc.yale.edu/applications/modules). EasyBuild can also be used to install software locally within your storage space.

When you install a new software package, EasyBuild performs the following steps:

*finds the easyconfig file matching the name you specify 
*gets sources(either downloaded or found in source path)
*configures
*builds
*installs
*generates module
 
## Get Started
To get started with installing software with EasyBuild, request an interactive session on the oldest available nodes and load the EasyBuild module:

```
salloc --cpus-per-task 4 --constraint oldest 
module load EasyBuild
```

## Configure EasyBuild
Some of the important configurations settings are:

*[Source path](https://docs.easybuild.io/configuration/#sourcepath): parent path of the directory for software source and install files
*[Build path](https://docs.easybuild.io/configuration/#buildpath): parent path of the temporaty directory for building software packages
*[Software and module install path](https://docs.easybuild.io/configuration/#installpath): by default,software install path is `$HOME/.local/easybuild/software` and module install path is `$HOME/.local/easybuild/modules/all`. 

You can look up the current configuration of EasyBuild with the following command:
```
eb --show-config

#
# Current EasyBuild configuration
# (C: command line argument, D: default value, E: environment variable, F: configuration file)
#
buildpath      (D) = /home/testuser/.local/easybuild/build
containerpath  (D) = /home/testuser/.local/easybuild/containers
installpath    (D) = /home/testuser/.local/easybuild
repositorypath (D) = /home/testuser/.local/easybuild/ebfiles_repo
robot-paths    (D) = /vast/palmer/apps/avx2/software/EasyBuild/4.9.3/easybuild/easyconfigs
sourcepath     (D) = /home/testuser/.local/easybuild/sources
```
If you wish to change any of these paths, you can do so using several methods including command-line arguments, environment variables and configuration files. For more details, take a look at the [documentation](https://docs.easybuild.io/configuration/). 

For example, if you would like to use a configuration file, please create a `config.cfg` file in `$HOME/.config/easybuild`:
```
cat $HOME/.config/easybuild/config.cfg

[config]
buildpath=/dev/shm/%(USER)s/build
installpath=/gpfs/gibbs/project/testuser/testuser/apps
sourcepath=/gpfs/gibbs/project/testuser/testuser/source

```
This configuration will change the output of `eb --show-config` to:
```
#
# Current EasyBuild configuration
# (C: command line argument, D: default value, E: environment variable, F: configuration file)
#
buildpath      (F) = /dev/shm/testuser/build
containerpath  (D) = /home/testuser/.local/easybuild/containers
installpath    (F) = /gpfs/gibbs/project/testuser/testuser/apps
repositorypath (D) = /home/testuser/.local/easybuild/ebfiles_repo
robot-paths    (D) = /vast/palmer/apps/avx2/software/EasyBuild/4.9.3/easybuild/easyconfigs
sourcepath     (F) = /gpfs/gibbs/project/testuser/testuser/source
```

## Search for Easyconfig files
To install software with EasyBuild, you need easyconfig files. Easyconfig files specify build parameters such as name, toolchain, sources, and dependencies. To searc for an existing easyconfig file for a specific softwar in the EasyBuild repository, you can use the `--search` or `-S` option:

```
eb -S HPCG

== found valid index for /vast/palmer/apps/avx2/software/EasyBuild/4.9.3/easybuild/easyconfigs, so using it...
CFGS1=/vast/palmer/apps/avx2/software/EasyBuild/4.9.3/easybuild/easyconfigs
 * $CFGS1/h/HPCG/HPCG-3.0-foss-2016b.eb
 * $CFGS1/h/HPCG/HPCG-3.0-foss-2018b.eb
 * $CFGS1/h/HPCG/HPCG-3.0-intel-2018b.eb
 * $CFGS1/h/HPCG/HPCG-3.1-foss-2018b.eb
 * $CFGS1/h/HPCG/HPCG-3.1-foss-2021a.eb
 * $CFGS1/h/HPCG/HPCG-3.1-foss-2021b.eb
 * $CFGS1/h/HPCG/HPCG-3.1-foss-2022a.eb
 * $CFGS1/h/HPCG/HPCG-3.1-foss-2022b.eb
 * $CFGS1/h/HPCG/HPCG-3.1-foss-2023a.eb
 * $CFGS1/h/HPCG/HPCG-3.1-intel-2018b.eb
 * $CFGS1/h/HPCG/HPCG-3.1-intel-2021a.eb
 * $CFGS1/h/HPCG/HPCG-3.1-intel-2021b.eb
 * $CFGS1/h/HPCG/HPCG-3.1-intel-2022a.eb
 * $CFGS1/h/HPCG/HPCG-3.1-intel-2022b.eb
 * $CFGS1/h/HPCG/HPCG-3.1-intel-2023a.eb
 * $CFGS1/h/HPCG/HPCG-3.1_fix-loop-upper-bound-variable-to-be-explicitly-designated-as-shared.patch

Note: 2 matching archived easyconfig(s) found, use --consider-archived-easyconfigs to see them

``` 

The config file typically has the name format `software-version-toolchain-version.eb`. Make sure to choose easyconfig files that uses the available [toolchains](https://docs.ycrc.yale.edu/applications/toolchains/) on our clusters. If you wish to edit the easyconfig file, copy and paste it in your own cluster space. For example:

```
cp /vast/palmer/apps/avx2/software/EasyBuild/4.9.3/easybuild/easyconfigs/h/HPCG/HPCG-3.1-intel-2022b.eb $HOME
```

Let's say we added a new patch and `versionsuffix = '-patched'` to the easyconfig file. If you change source files and patches in the easyconfig files, please update the [checksums](https://docs.easybuild.io/writing-easyconfig-files/?h=inject#common_easyconfig_param_sources):

```
eb --inject-checksums --force HPCG-3.1-intel-2022b.eb
```

## Install with EasyBuild
Before you install software with EasyBuild, you can perform a dry-run installation of software:
```
eb HPCG-3.1-intel-2022b.eb --dry-run
```
This will list all dependent software packages and indicate whether they are already installed as modules on the cluster.  

To install a software and create a module, run the following command:
```
eb HPCG-3.1-intel-2022b.eb
```

## Use locally installed modules
You can use the command:
```
module use $HOME/.local/easybuild/modules/all
module load HPCG/3.1-intel-2022b-patched
``
then `module avail` command will display modules installed locally.

You can also update $MODULEPATH in your $HOME/.bashrc file. Add this line:
```
export MODULEPATH=$MODULEPATH:$HOME/.local/easybuild/modules/all
```













