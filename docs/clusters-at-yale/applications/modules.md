# Load Software with Modules

To facilitate the diverse work that happens on the YCRC clusters we compile, install, and manage software packages separately from those installed in standard system directories. We use [EasyBuild](https://docs.easybuild.io/en/latest) to build, install, and manage packages. You can access these packages as [Lmod](https://lmod.readthedocs.io/en/latest) modules. The modules involving compiled software are arranged into hierarchical [toolchains](/clusters-at-yale/applications/toolchains) that make dependencies more consistent when you load multiple modules.

!!! warning
    Avoid loading Python or R modules and [conda](/clusters-at-yale/guides/conda) environments. This will almost always break something.

## Find Modules

### All Available Modules

To list all available modules, run:

``` bash
module avail
```

### Search For Modules

You can search for modules or extensions with `spider` and `avail`. For example, to find and list all Python version 3 modules, run:

``` bash
module avail python/3
```

To find any module or extension that mentions python in its name or description, use the command:

``` bash
module spider python
```

### Get Module Help

You can get a brief description of a module and the url to the software's homepage by running:

``` bash
module help modulename/version
```

If you don't find a commonly used software package you require, [contact us](/#get-help) with a software installation request. Otherwise, check out [our installation guides](/clusters-at-yale/applications) to install it for yourself.

## Load and Unload Modules

### Load

The `module load` command modifies your environment so you can use the specified software package(s).

- This command is case-sensitive to module names.
- The `module load` command will load dependencies as needed, you don't need to load them separately.
- For [batch jobs](/clusters-at-yale/job-scheduling/#batch-jobs), add `module load` command(s) to your submission script.

For example, to load `Python` version `3.8.6` and `BLAST+` version `2.11.0`, find modules with matching [toolchain](/clusters-at-yale/applications/toolchains) suffixes and run the command:

``` bash
module load Python/3.8.6-GCCcore-10.2.0 BLAST+/2.11.0-GCCcore-10.2.0
```

Lmod will add `python` and the BLAST commands to your environment.  Since both of these modules were built with the `GCCcore/10.2.0` [toolchain](/clusters-at-yale/applications/toolchains) module, they will not load conflicting libraries. Recall you can see the other modules that were loaded by running `module list`.

!!! tip "Module Defaults"
    As new versions of software get installed and others are [deprecated](/clusters-at-yale/applications/lifecycle), the default module version can change over time. It is best practice to note the specific module versions you are using for a project and load those explicitly, e.g. `module load Python/3.8.6-GCCcore-10.2.0` not `module load Python`. This makes your work more reproducible and less likely to change unexpectedly in the future.

### Unload

You can also unload a specific module that you've previously loaded:

``` bash
module unload R
```

Or unload all modules at once with:

``` bash
module purge
```

!!! warning "Purge Lightly"
    `module purge` will alert you to a sticky module that is always loaded called `StdEnv`. Avoid unloading `StdEnv` unless explicitly told to do so, othewise you will lose some important setup for the cluster you are on.

### Module Collections

#### Save Collections

It can be a pain to enter a long list of modules every time you return to a project. Module collections allow you to create sets of modules to load together. This method is particularly useful if you have two or more module sets that may [conflict](/clusters-at-yale/applications/toolchains/#what-versions-match) with one another.

Save a collection of modules by first loading all the modules you want to save together then run:

``` bash
module save environment_name
```

(replace `environment_name` with something more meaningful to you)

#### Restore Collections

Load a collection with `module restore`:

``` bash
module restore environment_name
```

To modify a collection: `restore` it, make the desired changes by `load`ing and/or `unload`ing modules, then `save` it to the same name. 

#### List Collections

To get a list of your collections, run:

``` bash
module savelist
```

## Environment Variables

To refer to the directory where the software from a module is stored, you can use the environment variable `$EBROOTMODULENAME` where MODULENAME is the name of the module in all caps with no spaces. This can be useful for finding the executables, libraries, or readme files that are included with the software:

```bash
[netid@node ~ ]$ module load SAMtools
[netid@node ~ ]$ echo $EBVERSIONSAMTOOLS
1.11
[netid@node ~ ]$ ls $EBROOTSAMTOOLS
bin  easybuild  include  lib  lib64  share
[netid@node ~ ]$ ls $EBROOTSAMTOOLS/bin
ace2sam             maq2sam-short       psl2sam.pl             soap2sam.pl
blast2sam.pl        md5fa               r2plot.lua             vcfutils.lua
bowtie2sam.pl       md5sum-lite         sam2vcf.pl             wgsim
export2sam.pl       novo2sam.pl         samtools               wgsim_eval.pl
interpolate_sam.pl  plot-ampliconstats  samtools.pl            zoom2sam.pl
maq2sam-long        plot-bamstats       seq_cache_populate.pl
```

## Further Reading

You can view documentation while on the cluster using the command:

``` bash
man module
```

There is even more information at the [offical Lmod website](http://www.tacc.utexas.edu/tacc-projects/lmod).
