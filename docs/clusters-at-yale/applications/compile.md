# Build Software

How to get software you need up and running on the clusters.

## *caveat emptor*

We usually recommend either use existing [software modules](/clusters-at-yale/applications/modules), [Anaconda](/clusters-at-yale/applications/guides/conda), [Singularity](/clusters-at-yale/applications/guides/singularity), or pre-compiled software where available. However, there are cases where compiling applications is necessary or desired. This can be because the pre-compiled version isn't readily available/compatible or because compiling applications on the cluster will make an appreciable difference in performance. It is also the case that many R packages are compiled at install time.

When compiling applications on the clusters, it is important to consider the ways in which you expect to run the application you are endeavoring to get working. If you want to be able to run jobs calling your application any node on the cluster, you will need to target the oldest hardware available so that newer optimizations are not used that will fail on some nodes. If your application is already quite specialized (e.g. needs GPUs or brand-new CPU instructions), you will want to compile it natively for the subset of compute nodes on which your jobs will run. This decision is often a trade-off between faster individual jobs or jobs that can run on more nodes at once.

Each of the cluster pages (see the [clusters index](/clusters-at-yale/clusters) for a list) has a "Compute Node Configurations" section where nodes are roughly listed from oldest to newest.

## Conventions

### Local Install

Because you don't have admin/root/sudo privileges on the clusters, you won't be able to use `sudo` and a package manager like `apt`, `yum`, etc.; You will need to adapt install instructions to allow for what is called a local or user install. If you prefer or require this method, you should create a singularity container image (see our [Singularity guide](/clusters-at-yale/applications/guides/singularity/)), then run it on the cluster.

For things to work smoothly you will need to choose and stick with a prefix, or path to your installed applications and libraries. We recommend this be either in your home or project directory, something like `~/software` or `/path/to/project/software`. Make sure you have created it before continuing.

!!! tip
    If you choose a project directory prefix, it will be easier to share your applications with lab mates or other cluster users. Just make sure to use the true path (the one returned by `mydirectories`).

Once you've chosen a prefix you will want to add any directory with executables you want to run to your `PATH` environment variable, and any directores with libraries that your application(s) link to your `LD_LIBRARY_PATH` environment variable. Each of these tell your shell where to look when you call your application without specifying an absolute path to it. To set these variables permanently, add the following to the end of your `~/.bashrc` file:

``` bash
# local installs
export MY_PREFIX=~/software
export PATH=$MY_PREFIX/bin:$PATH
export LD_LIBRARY_PATH=$MY_PREFIX/lib:$LD_LIBRARY_PATH
```

For the remainder of the guide we'll use the `$MY_PREFIX` variable to refer to the prefix. See below or your application's install instructions for exactly how to specify your prefix at build/install time.

### Dependencies

You will need to develop a build strategy that works for you and stay consistent. If you're happy using libraries and [toolchains](/clusters-at-yale/applications/easybuild/#toolchains) that are already available on the cluster as dependencies (recommended), feel free to create [module collections](/clusters-at-yale/applications/modules/#module-collections) that serve as your environments. If you prefer to completely build your own software tree, that is ok too. Whichever route you choose, try to stick with the same version of dependencies (e.g. MPI, zlib, numpy) and compiler you're using (e.g. GCC, intel). We find that unless absolutely necessary, the newest version of a compiler or library might not be the most compatible with a wide array of scientific software so you may want to step back a few versions or try using what was available at the time your application was being developed.

## Autotools (`configure`/`make`)

If your application includes instructions to run `./bootstrap`, `./autogen.sh`, `./configure` or `make`, it is using the [GNU Build System](https://en.wikipedia.org/wiki/GNU_Build_System). 

### `configure`

If you are instructed to run `./configure` to generate a Makefile, specify your prefix with the `--prefix` option. This creates a file, usually named `Makefile` that is a recipe for `make` to use to build your application.

``` bash
export MY_PREFIX=~/software
./configure --prefix=$MY_PREFIX
```

### `make install`

If your configure ran properly, `make install` should properly place your application in your prefix directory. If there is no install target specified for your application, you can either run `make` and copy the application to your `$MY_PREFIX/bin` directory or build it somewhere in `$MY_PREFIX` and add its relevant paths to your `PATH` and/or `LD_LIBRARY_PATH` environment variables in your `~/.bashrc` file as shown in the [local install](#local-install) section.

## CMake

[CMake](https://en.wikipedia.org/wiki/CMake) is a popular cross-platform build system. On a linux system, CMake will create a `Makefile` in a step analogous to `./configure`. It is common to create a build directory then run the `cmake` and `make` commands from there. Below is what installing to your `$MY_DIRECTORY` prefix might look like with CMake. CMake instructions also tend to link together the build process onto on line with `&&`, which tells your shell to only continue to the next command if the previous one exited without error.

``` bash
export MY_PREFIX=~/software
mkdir build && cd build && cmake -DCMAKE_INSTALL_PREFIX=$MY_PREFIX .. && make && make install
```