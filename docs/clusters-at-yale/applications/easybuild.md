# Toolchains and EasyBuild

We use a build and installation framework called [EasyBuild](https://easybuild.readthedocs.io/en/latest/) that connects the software we compile and maintain on the clusters with the [module system](/clusters-at-yale/applications/modules) that makes it available to you.

## Toolchains

When we install software, we use pre-defined build environments called toolchains.
These are modules that include core compilers and libraries (e.g. `GCC`, `OpenMPI`, `zlib`).
We do this for two main reasons.
One is to try to keep our build process simpler.
The other is so that you can load two different modules for software built with the same toolchain and expect everything to work.
The two common toolchains you will interact with are [`foss`](https://easybuild.readthedocs.io/en/latest/Common-toolchains.html#component-versions-in-foss-toolchain) and [`intel`](https://easybuild.readthedocs.io/en/latest/Common-toolchains.html#component-versions-in-intel-toolchain).
Each of these have module versions corresponding to the year they were built.
Toolchain name and version information is appended to the name of a module so it is clear to us and to the module system what should be compatible.
An example would be `Python/2.7.12-foss-2016b`, where the software name is `Python`, version `2.7.12`, built with the `foss` toolchain version `2016b`.
The easiest way to see what software a toolchain includes is to load it and then list loaded modules.

```
[be59@farnam2 ~]$ module load foss/2016b
[be59@farnam2 ~]$ module list

Currently Loaded Modules:
  1) StdEnv                        (S)   7) OpenMPI/1.10.3-GCC-5.4.0-2.26
  2) GCCcore/5.4.0                       8) OpenBLAS/0.2.18-GCC-5.4.0-2.26-LAPACK-3.6.1
  3) binutils/2.26-GCCcore-5.4.0         9) gompi/2016b
  4) GCC/5.4.0-2.26                     10) FFTW/3.3.4-gompi-2016b
  5) numactl/2.0.11-GCC-5.4.0-2.26      11) ScaLAPACK/2.0.2-gompi-2016b-OpenBLAS-0.2.18-LAPACK-3.6.1
  6) hwloc/1.11.3-GCC-5.4.0-2.26        12) foss/2016b

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

The takeaway here is that you should try to use modules that match their `foss` or `intel` identifiers.

## Toolchain Trees

The one place this can get a little complicated is that there are various levels to a given toolchain depending on how many libraries are included.
For example, `foss/2018a` is a parent toolchain to `GCCcore/6.4.0` since it includes GCC 6.4.0 and OpenMPI 2.1.2. 

### Base toolchains:
`GCCcore` - GCC compiler  
`iccifort` - Intel compiler (GCCcore is actually a also sub-toolchain of
iccifort)

### Toolchains with MPI:
`gompi` - GCCcore + OpenMPI  
`iimpi` - iccifort + IntelMPI  
`iompi` - iccifort + OpenMPI  

### Full toolchains (also include math libraries):
`foss` - gompi + OpenBLAS + ScalaPack  
`intel` - iimpi + Intel MKL  
`iomkl `- iompi + Intel MKL  


For installations that use MPI and a math library, you want to choose a full toolchain and epoch and then look
modules that contain that toolchain or its sub-toolchains to ensure compatibility.
You can run `module display foss/2016b` to see which versions of the compiler and libraries it includes.

## Environment Variables

If you ever want to refer to the directory where the software from a module is stored, you can use the environment variable `$EBROOTMODULENAME` where modulename is the name of the module in all caps with no spaces. This can be useful for finding the executables, libraries, or readme files that are included with the software:

```
[be59@farnam2 ~]$ module load SAMtools/1.9-foss-2016b
[be59@farnam2 ~]$ ls $EBROOTSAMTOOLS
bin  easybuild  include  lib  share
[be59@farnam2 ~]$ ls $EBROOTSAMTOOLS/bin
ace2sam        interpolate_sam.pl  md5sum-lite    r2plot.lua   seq_cache_populate.pl  wgsim
blast2sam.pl   maq2sam-long        novo2sam.pl    sam2vcf.pl   soap2sam.pl            wgsim_eval.pl
bowtie2sam.pl  maq2sam-short       plot-bamstats  samtools     varfilter.py           zoom2sam.pl
export2sam.pl  md5fa               psl2sam.pl     samtools.pl  vcfutils.lua
```
