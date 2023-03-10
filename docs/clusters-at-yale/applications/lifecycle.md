# Software Module Lifecycle

To keep the YCRC cluster [software modules](/clusters-at-yale/applications/modules) catalogs tidy, relevant, and up to date, we periodically [deprecate](https://en.wikipedia.org/wiki/Deprecation#Software) and introduce modules.

## Deprecated Modules

 The two major criteria we use to decide which modules to deprecate are:

- A software module has not been used much in the past year
- We are ending support for the toolchain with which a module was built

As we deprecate modules, every time you load a module that has been marked for removal a warning message will appear. The message state when the module will no appear in the module list. If you see such a message, we recommend you update your project to use a supported module as soon as possible or [contacting us](/#get-help) for help. 

## Toolchain Support

The YCRC maintains a rolling two [toolchain](/clusters-at-yale/applications/toolchains) version support model. At any given time on a cluster, we aim to support two versions of each of the major toolchains, [`foss`](/clusters-at-yale/applications/toolchains/#free-open-source-software-foss) and [`intel`](/clusters-at-yale/applications/toolchains/#intel). The two versions are separated by two years and new software is typically installed with the later version. When we introduce a new toolchain version, we phase out support for the oldest by marking software in that toolchain for deprecation. A few months later, software in the oldest toolchain version will be removed from the module list and no longer supported by the YCRC.