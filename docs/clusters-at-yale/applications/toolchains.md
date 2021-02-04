# Software Module Toolchains

The YCRC uses a framework called [EasyBuild](https://easybuild.readthedocs.io/en/latest/) to build and install the software you access via the [module system](/clusters-at-yale/applications/modules).

## Toolchains

When we install software, we use pre-defined build environment modules called toolchains. These are modules that include dependencies like compilers and libraries such as GCC, OpenMPI, CUDA, etc. We do this to keep our build process simpler, and to ensure that sets of software modules loaded together function properly. The two groups of toolchains we use on the YCRC clusters are [`foss`](https://easybuild.readthedocs.io/en/latest/Common-toolchains.html#component-versions-in-foss-toolchain) and [`intel`](https://easybuild.readthedocs.io/en/latest/Common-toolchains.html#component-versions-in-intel-toolchain), which hierarchically include some shared sub-toolchains. Toolchains will have versions associated with the version of the compiler and/or when the toolchain was composed. Toolchain names and versions are appended as suffixes in module names. This tells you that a module was built with that toolchain and which other modules are compatible with it. 

### Free Open Source Software (`foss`)

The `foss` toolchains are versioned with a yearletter scheme, e.g. `foss/2018b` is the second `foss` toolchain composed in 2018. Software modules that were built with a sub-toolchain, e.g. `GCCcore`, are still safe to load with their parents as long as their versions match. Below is a tree depicting which toolchains inherit each other.

``` text
foss: gompi + FFTW, OpenBLAS, ScaLAPACK
└── gompi: GCC + OpenMPI
    └── GCC: GCCcore + zlib, binutils
        └── GCCcore: GNU Compiler Collection

fosscuda: gompic + FFTW, OpenBLAS, ScaLAPACK
└── gompic: gcccuda + CUDA-enabled OpenMPI
    └── gcccuda: GCC + CUDA
        └── GCC: GCCcore + zlib, binutils
            └── GCCcore: GNU Compiler Collection
```

### Intel

The YCRC licenses Intel Parallel Studio XE (Intel oneAPI Base & HPC Toolkit coming soon). The `intel` and `iomkl` toolchains are versioned with a yearletter scheme, e.g. `intel/2018b` is the second `intel` toolchain composed in 2018. The major difference between `iomkl` and `intel` is MPI - `intel` uses Intel's MPI implementation and `iomkl` uses OpenMPI. Below is a tree depicting which toolchains inherit each other.

``` text
iomkl: iompi + Intel Math Kernel Library
└── iompi: iccifort + OpenMPI
    └── iccifort: Intel compilers
        └── GCCcore: GNU Compiler Collection
intel: iimpi + Intel Math Kernel Library
└── iimpi: iccifort + Intel MPI
    └── iccifort: Intel C/C++/Fortran compilers
        └── GCCcore: GNU Compiler Collection
```

## What Versions Match?

To see what versions of sub-toolchains are compatible with their parents, load a `foss` or `intel` module of interest and run `module list`.

```bash
[netid@node ~]$ module load foss/2018b
[netid@node ~]$ module list

Currently Loaded Modules:
  1) StdEnv                       (S)   8) OpenMPI/3.1.1-GCC-7.3.0-2.30
  2) GCCcore/7.3.0                      9) OpenBLAS/0.3.1-GCC-7.3.0-2.30
  3) binutils/2.30-GCCcore-7.3.0       10) gompi/2018b
  4) GCC/7.3.0-2.30                    11) FFTW/3.3.8-gompi-2018b
  5) zlib/1.2.11-GCCcore-7.3.0         12) ScaLAPACK/2.0.2-gompi-2018b-OpenBLAS-0.3.1
  6) numactl/2.0.11-GCCcore-7.3.0      13) foss/2018b
  7) hwloc/1.11.10-GCCcore-7.3.0

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```
Here you see that `foss/2018b` includes `GCCcore/7.3.0`, so modules with either the `foss-2018b` or `GCCcore-7.3.0` should be compatible.