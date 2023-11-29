# Rebuilding conda environemnts

There are two concepts for rebuilding conda environments:

1. a copy of an existing environment, with identical versions of each package
2. a fresh build following the same steps taken to creat the first environment (letting unspecified versions float)

This short doc will walk through recommended approaches to both styles of exporting and rebuilding a generic environment named `test` containing python, jupyter, numpy, and scipy.


## Full export including dependencies

To export the exact versions of each package installed (including all dependencies) run:

```sh
module load miniconda
conda env export --no-builds --name test | grep -v prefix > test_export.yaml

```

This yaml file is ~230 lines long and contains every package that is installed in the `test` environment.

The conda export command includes information about the path where it was installed (i.e. the `prefix`).
To remove this hard-coded path, we need to remove the line in this print out related to the "prefix".


## Export only specified packages

If we simply wish to rebuild the environment using the steps previously employed to create it, we can replace `--no-builds` with `--from-history`. 
```sh
module load miniconda
conda env export --from-history --name test | grep -v prefix > test_export.yaml

```

This is a much smaller file, ~10 lines, and only lists the packages explicitly installed:

```yml
name: test
channels:
  - conda-forge
  - defaults
  - bioconda
dependencies:
  - scipy
  - numpy=1.21
  - jupyter
  - python=3.8

```

In this environment, the versions of python and numpy were pinned during installation, but scipy and jupyter were left to get the most recent compatible version.



## Build new environment

To create a new environment using all the enumerated pacakges:

```sh
module load miniconda
conda env create --file test_export.yaml

```

This will create a new environment with the same name `test`.
The yaml file can be edited to change the name of the new environment.

