# Software Module Toolchains

The YCRC uses a framework called [EasyBuild](https://easybuild.readthedocs.io/en/latest/) to build and install the software you access via the [module system](/clusters-at-yale/applications/modules).

## Toolchains

When we install software, we use pre-defined build environment modules called toolchains. These are modules that include dependencies like compilers and libraries such as GCC, OpenMPI, CUDA, etc. We do this to keep our build process simpler, and to ensure that sets of software modules loaded together function properly. The two groups of toolchains we use on the YCRC clusters are [`foss`](https://easybuild.readthedocs.io/en/latest/Common-toolchains.html#component-versions-in-foss-toolchain) and [`intel`](https://easybuild.readthedocs.io/en/latest/Common-toolchains.html#component-versions-in-intel-toolchain), which hierarchically include some shared sub-toolchains. Toolchains will have versions associated with the version of the compiler and/or when the toolchain was composed. Toolchain names and versions are appended as suffixes in module names. This tells you that a module was built with that toolchain and which other modules are compatible with it. The YCRC maintains a rolling two toolchain version support model. The toolchain versions supported on each cluster are listed in the [Module Lifecycle](/clusters-at-yale/applications/lifecycle) documentation.

### Free Open Source Software (`foss`)

The `foss` toolchains are versioned with a yearletter scheme, e.g. `foss/2020b` is the second `foss` toolchain composed in 2020. Software modules that were built with a sub-toolchain, e.g. `GCCcore`, are still safe to load with their parents as long as their versions match. The major difference between `foss` and `fosscuda` is that `fosscuda` includes CUDA and builds applications for GPUs by default. You shoould only use `fosscuda` modules on nodes with [GPUs](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus). Below is a tree depicting which toolchains inherit each other.

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

The YCRC licenses Intel Parallel Studio XE (Intel oneAPI Base & HPC Toolkit coming soon). The `intel` and `iomkl` toolchains are versioned with a yearletter scheme, e.g. `intel/2020b` is the second `intel` toolchain composed in 2020. The major difference between `iomkl` and `intel` is MPI - `intel` uses Intel's MPI implementation and `iomkl` uses OpenMPI. Below is a tree depicting which toolchains inherit each other.

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
[netid@node ~]$ module load foss/2020b
[netid@node ~]$ module list

Currently Loaded Modules:
  1) StdEnv                        (S)   7) XZ/5.2.5-GCCcore-10.2.0           13) OpenMPI/4.0.5-GCC-10.2.0
  2) GCCcore/10.2.0                      8) libxml2/2.9.10-GCCcore-10.2.0     14) OpenBLAS/0.3.12-GCC-10.2.0
  3) zlib/1.2.11-GCCcore-10.2.0          9) libpciaccess/0.16-GCCcore-10.2.0  15) gompi/2020b
  4) binutils/2.35-GCCcore-10.2.0       10) hwloc/2.2.0-GCCcore-10.2.0        16) FFTW/3.3.8-gompi-2020b
  5) GCC/10.2.0                         11) UCX/1.9.0-GCCcore-10.2.0          17) ScaLAPACK/2.1.0-gompi-2020b
  6) numactl/2.0.13-GCCcore-10.2.0      12) libfabric/1.11.0-GCCcore-10.2.0   18) foss/2020b

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

Here you see that `foss/2020b` includes `GCCcore/10.2.0`, so modules with either the `foss-2020b` or `GCCcore-10.2.0` should be compatible.