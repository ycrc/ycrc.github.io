# Software Module Lifecycle

To keep the YCRC cluster [software modules](/clusters-at-yale/applications/modules) catalog tidy, relevant, and up to date, we periodically [deprecate](https://en.wikipedia.org/wiki/Deprecation#Software) and introduce modules.

## Deprecated Modules

 The two major criteria we use to decide what modules to deprecate are:

- Has a software module has been used much in the past year? If not, deprecate.
- Are we ending support for the toolchain a module was built with? If so, deprecate.

After we deprecate modules, we print a warning message every time you load a module that has been marked for deprecation. The message tells you how long you have before the module disappears. We recommend you get started changing what needs to be changed to use new software for your project or [contacting us](/#get-help) for help in this planning. 

## Toolchain Support

We have adopted a rolling two [toolchain](/clusters-at-yale/applications/toolchains) support model. This means at any given time on a cluster, we aim to have no more than two versions of the major toolchains [`foss`](/clusters-at-yale/applications/toolchains/#free-open-source-software-foss) and [`intel`](/clusters-at-yale/applications/toolchains/#intel). The two versions are a newer and older version, where we typically target the newer version when building software. When we begin testing a new toolchain version, we phase out support for the oldest by marking it as deprecated. Once testing is complete and a few months have passed, we remove the oldest toolchain. 

## Spring 2021 Deprecation cycle

Beginning in February 2021, we are marking modules built with unsupported toolchains as deprecated. Here is a list of the toolchains we are removing and introducing. If you notice a module you are using that is going away without a newer version to use, please [contact us](/#get-help) before May so we can get a replacement installed.

### [Grace](/clusters-at-yale/clusters/grace) and [Milgram](/clusters-at-yale/clusters/milgram)

#### Deprecated software (will be removed by May 31, 2021):

- Modules built with a 2016b toolchain, GCCcore/5.x, or iccifort/2016.3.210
- Unused modules

#### Supported software

- Modules built with a 2018a toolchain, GCCcore/6.4.0 or iccifort/2018.1.163
- Modules built  with a 2018b toolchain, GCCcore/7.3.0 or iccifort/2018.3.222
- Modules built with a 2020b toolchain, GCCcore/10.2.0 or iccifort/2020.4.304 (new)
- Commonly used modules not otherwise deprecated

### [Farnam](/clusters-at-yale/clusters/farnam) and [Ruddle](/clusters-at-yale/clusters/ruddle)

#### Deprecated software (will be removed by May 31, 2021):

- Modules built with 2016a, 2016b, 2017a, or 2017b toolchains or GCCcore/4.x, GCCcore/5.x, GCCcore/6.x
- Unused modules

#### Supported software

- Modules built with a 2018b toolchain or GCCcore/7.3.0
- Modules built with a 2020b toolchain or GCCcore/10.2.0 (new)
- Commonly used modules not otherwise deprecated
