# Containers

!!!warning
    The Singularity project has been renamed [Apptainer](https://apptainer.org). Everything should still work the same, including the 'singularity' command.  If you find it not working as expected, please [contact us](https://docs.ycrc.yale.edu/#get-help).

[Apptainer](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177459) (formerly Singularity) is a Linux container technology that is well suited to use in shared-user environments such as the [clusters](/clusters) we maintain at Yale. It is similar to [Docker](https://docs.docker.com/); You can bring with you a stack of software, libraries, and a Linux operating system that is independent of the host computer you run the container on. This can be very useful if you want to share your software environment with other researchers or yourself across several computers. Because Apptainer containers run as the user that started them and mount home directories by default, you can usually see the data you're interested in working on that is stored on a host computer without any extra work.

Below we will outline some common use cases covering the creation and use of containers. There is also excellent documentation available on the full and official [user guide for Apptainer](https://apptainer.org/docs/user/main/). We are happy to help, just [contact us](/#get-help) with your questions.

!!!warning
    On the Yale clusters, **Apptainer is not installed on login nodes.** You will need to run it from compute nodes.

## Apptainer Containers

Images are the file(s) you use to run your container. Apptainer images are single files that usually end in `.sif` and are read-only by default, meaning changes you make to the environment inside the container are not persistent.

## Use a Pre-existing Container

If someone has already built a container that suits your needs, you can use it directly. Apptainer images are single files that [can be transferred](/data/transfer) to the clusters. You can fetch images from container registries such as [Docker Hub](https://hub.docker.com/explore/) or [Singularity Hub](https://singularityhub.github.io/singularityhub-docs/) (no longer updated). Container images can take up a lot of disk space (dozens of gigabytes), so you may want to change the default location Apptainer uses to cache these files. To do this before getting started, you should add something like the example below to to your `~/.bashrc` file:

``` bash
# set APPTAINER_CACHEDIR if you want to pull files (which can get big) somewhere other than $HOME/.apptainer
# e.g.
export APPTAINER_CACHEDIR=~/scratch60/.apptainer
```

Here are some examples of getting containers already built by someone else with apptainer:

``` bash
# from Docker Hub (https://hub.docker.com/)
apptainer build ubuntu-18.10.sif docker://ubuntu:18.10
apptainer build tensorflow-10.0-py3.sif docker://tensorflow/tensorflow:1.10.0-py3

# from Singularity Hub (no longer updated)
apptainer build bioconvert-latest.sif shub://biokit/bioconvert:latest
```

## Build Your Own Container

You can define a container image to be exactly how you want/need it to be, including applications, libraries, and files of your choosing with a [definition file](https://apptainer.org/docs/user/main/quick_start.html#apptainer-definition-files).
Apptainer definition files are similar to Docker's `Dockerfile`, but use different syntax.
To build a container from a definition file, you need administrative privileges on a Linux machine where [Apptainer is installed](https://apptainer.org/docs/user/main/quick_start.html#quick-installation-steps).


For full definition files and more documentation please see [the Apptainer site](https://apptainer.org/docs/user/main/definition_files.html).


### Header

Every container definition must begin with a header that defines what image to start with, or bootstrap from. This can be an official Linux distribution or someone else's container that gets you nearly what you want.

To start from Ubuntu Bionic Beaver (18.04 LTS):

``` bash
Bootstrap: docker
From: ubuntu:18.04
```

Or an Nvidia developer image

``` bash
Bootstrap: docker
From: nvidia/cuda:9.2-cudnn7-devel-ubuntu18.04
```

The rest of the sections all begin with `%` and the section name. You will see section contents indented by convention, but this is not required.

### %labels

The labels section allows you to define metadata for your container:

``` bash
%labels
    Name
    Maintainer "YCRC Support Team" <hpc@yale.edu>Version v99.9
    Architecture x86_64
    URL https://research.computing.yale.edu/</hpc@yale.edu>
```

You can examine container metadata with the `apptainer inspect` command.

### %files

If you'd like to copy any files from the system you are building on, you do so in the %files section. Each line in the files section is a pair of source and destination paths, where the source is on your host system, and destination is a path in the container.

``` bash
%files
    sample_data.tar /opt/sample_data/
    example_script.sh /opt/sample_data/
```

### %post

The post section is where you can run updates, installs, etc in your container to customize it.

``` bash
%post
    echo "Customizing Ubuntu"
    apt-get update
    apt-get -y install software-properties-common build-essential cmake
    add-apt-repository universe
    apt-get update
    apt-get -y libboost-all-dev libgl1-mesa-dev libglu1-mesa-dev
    cd /tmp
    git clone https://github.com/gitdudette/myapp && cd myapp
    # ... etc etc
```

### %environment

The environment section allows you to define environment variables for your container. These variables are available when you run the built container, not during its build.

``` bash
%environment
    export PATH=/opt/my_app/bin:$PATH
    export LD_LIBRARY_PATH=/opt/my_app/lib:$LD_LIBRARY_PATH
```

### Building

To finally build your container after saving your definition file as `my_app.def`, for example, you would run

``` bash
apptainer build my_app.sif my_app.def
```

## Use a Container Image

Once you have a container image, you can run it as a part of a batch job, or interactively.

### Interactively

To get a shell in a container so you can interactively work in its environment:

``` bash
apptainer shell --shell /bin/bash containername.sif
```

### In a Job Script

You can also run applications from your container non-interactively as you would in a batch job. If I wanted to run a script called `my_script.py` using my container's python:

``` bash
apptainer exec containername.sif python my_script.py
```

## Environment Variables

If you are unsure if you are running inside or outside your container, you can run:

``` bash
echo $APPTAINER_NAME
```

If you get back text, you are in your container.

If you'd like to pass environment variables into your container, you can do so by defining them prefixed with `APPTAINERENV_` . For Example:

``` bash
export APPTAINERENV_BLASTDB=/home/me/db/blast
apptainer exec my_blast_image.sif env | grep BLAST
```

Should return `BLASTDB=/home/me/db/blast`, which means you set the `BLASTDB` environment variable in the container properly.

## Additional Notes

### MPI

MPI support for Apptainer is relatively straight-forward. The only thing to watch is to make sure that you are using the same version of MPI inside your container as you are on the cluster.

### GPUs

You can use GPU-accelerated code inside your container, which will need most everything also installed in your container (e.g. CUDA, cuDNN). In order for your applications to have access to the right drivers on the host machine, use the `--nv` flag. For example:

``` bash
apptainer exec --nv tensorflow-10.0-py3.sif python ./my-tf-model.py
```

### Home Directories

Sometimes the maintainer of a Docker container you are trying to use installed software into a special user's home directory. If you need access to someone's home directory that exists in the container and not on the host, you should add the `--contain` option. Unfortunately, you will also then have to explicitly tell Apptainer about the paths that you want to use from inside the container with the [`--bind`](https://apptainer.org/docs/user/main/bind_paths_and_mounts.html) option.

``` bash
apptainer shell --shell /bin/bash --contain --bind /gpfs/gibbs/project/support/be59:/home/be59/project bioconvert-latest.sif
```
