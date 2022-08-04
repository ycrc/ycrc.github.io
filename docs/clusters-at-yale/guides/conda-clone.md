# Clone Conda Environments

During the Grace August 2022 maintenance, Loomis project directories were migrated to the Gibbs filesystem.
This move included numerous Conda environments which may no longer work properly after the migration.


## Clone to a New Name

A simple way to repair any broken environments is to use Conda's built-in `clone` option to create a new environment based on the packages installed in the existing one.
This is similar to exporting the contents of an environment and then building a new environment from that export, but it can be done in one step:

```sh
module load miniconda
conda create --name new_env --clone old_env
```

## `conda_mover.sh` Helper Script

To simplify things, we have developed a tool, `conda_mover.sh`, which will rebuild all your environments (or any specific ones provided by name) with the same environment name.

!!! Warning
    We recommend doing all of this actions on a compute node with at least 10G of memory to ensure `conda` will work properly.

The usage is as follows.

```sh
[netid@c16n01 ~]$ conda_mover.sh -h
A utility to clone multiple conda environments from existing location to the new project space
To specify the new path, set the PROJECT environment variable

Syntax: conda_mover.sh [-h|l|a|n NAME]
options:
h        Print this help
l        List all available environments
a        Clone all available environments
n NAME   Clone environment NAME
```

To list all known environments:

```sh
[netid@c16n01 ~]$ conda_mover.sh -l
```

### Rebuild an Environment

You can either rebuild a single environment at a time or all your environments using the helper script. 
Remember to load any relevant modules for supporting libraries where needed.

!!! Warning
    For more complex environments, such as those using both `pip` and `conda` or environments that use MPI,
    we recommend manually rebuilding the environment instead of cloning. [Contact us](/#get-help) if you need assistance.

To rebuild a single environment:

```sh
[netid@c16n01 ~]$ conda_mover.sh -n env_name
```

To rebuild all known environments:

```sh
[netid@c16n01 ~]$ conda_mover.sh -a
```

If you choose the rebuild all known environments (with `-a`), this may take a while, so it may be useful to launch as a batch job.
An example script is provided below.

```sh
#!/bin/bash

#SBATCH -p day
#SBATCH -t 6:00:00
#SBATCH -c 1
#SBATCH --mem-per-cpu=10G
#SBATCH --job-name conda_mover

module purge

/gpfs/gibbs/public/bin/conda_mover.sh -a

```
