# Software Module Lifecycle

To keep the YCRC cluster [software modules](/clusters-at-yale/applications/modules) catalogs tidy, relevant, and up to date, we periodically [deprecate](https://en.wikipedia.org/wiki/Deprecation#Software) and introduce modules.

## Deprecated Modules

 The two major criteria we use to decide which modules to deprecate are:

- A software module has not been used much in the past year
- We are ending support for the toolchain with which a module was built

As we deprecate modules, every time you load a module that has been marked for removal a warning message will appear. The message state when the module will no appear in the module list. If you see such a message, we recommend you update your project to use a supported module as soon as possible or [contacting us](/#get-help) for help. 

## Toolchain Support

The YCRC maintains a rolling two [toolchain](/clusters-at-yale/applications/toolchains) version support model. At any given time on a cluster, we aim to support two versions of each of the major toolchains, [`foss`](/clusters-at-yale/applications/toolchains/#free-open-source-software-foss) and [`intel`](/clusters-at-yale/applications/toolchains/#intel). The two versions are separated by two years and new software is typically installed with the later version. When we introduce a new toolchain version, we phase out support for the oldest by marking software in that toolchain for deprecation. A few months later, software in the oldest toolchain version will be removed from the module list and no longer supported by the YCRC.

## Spring 2021 Deprecation Cycle

In June 2021, we removed deprecated software and introduced a new epoch of toolchains. If a module you used in the past is no longer available and there is not a newer module available, please [contact us](/#get-help).

### [Grace](/clusters/grace) and [Milgram](/clusters/milgram)

#### Removed Software:

- Modules built with a 2016b toolchain, GCCcore/5.x, or iccifort/2016.3.210
- Unused modules

#### Supported Software

- Modules built with a 2018a toolchain, GCCcore/6.4.0 or iccifort/2018.1.163
- Modules built with a 2018b toolchain, GCCcore/7.3.0 or iccifort/2018.3.222 (Grace only)
- Modules built with a 2020b toolchain, GCCcore/10.2.0 or iccifort/2020.4.304 (new)
- Commonly used modules not otherwise deprecated

### [Farnam](/clusters/farnam) and [Ruddle](/clusters/ruddle)

#### Removed Software:

- Modules built with 2016a, 2016b, 2017a, or 2017b toolchains or GCCcore/4.x, GCCcore/5.x, GCCcore/6.x
- Unused modules

#### Supported Software

- Modules built with a 2018b toolchain or GCCcore/7.3.0
- Modules built with a 2020b toolchain or GCCcore/10.2.0 (new)
- Commonly used modules not otherwise deprecated