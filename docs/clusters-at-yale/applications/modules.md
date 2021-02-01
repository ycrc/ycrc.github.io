# Load Software with Modules

There are many software packages installed on the Yale clusters in addition to those installed in the standard system directories. This software has been [specifically installed](/clusters-at-yale/applications/toolchains) for use on our clusters at the request of our users. In order to manage these additional packages, the clusters use "module files". These module files allow you to easily specify which versions of which packages you want use.

## List All Loaded Modules

The `module list` command displays all of the module files that are currently loaded in your environment:

``` bash
module list
```

You may notice a module named `StdEnv` loaded by default. This module sets up your cluster environment; purging this module will make the modules we have installed unavailable.

## Find Available Modules

To list all available module files, execute:

``` bash
module avail
```

You can also list all module files whose name contains a specified string. For example, to find all Python module files, use:

``` bash
module avail python
```

!!!tip
    You can get a brief description of a module and the url to the software's homepage by running:
    `module help <modulename>`

If you don't find a commonly used software you require in the list of modules feel free [contact us](/#get-help) with a software installation request. Otherwise, check out [our installation guides](/clusters-at-yale/applications) to install it for yourself.

## Load and Unload Modules

The `module load` command is used to modify your environment so you can use a specified software package. For example, if you found and want to load `Python` version `2.7.13`, execute the command:

``` bash
module load Python/2.7.13-foss-2016b
```

This modifies the PATH environment variable (as well as a few others) so that your default Python interpreter is version `2.7.13`:

``` bash
[be59@farnam2 ~]$ python --version
Python 2.7.13
```

You don't have to specify the version. For example, if you want the default module version of R, use:

``` bash
module load R
```

You can also unload a module that you've previously loaded:

``` bash
module unload R
```

!!!warning
    Mixing and matching certain software can be tricky due to the way we build our software and modules. In short, make sure that the `foss` or `intel` in your module names match if they are present. For more information, see our [EasyBuild page](/clusters-at-yale/applications/toolchains).

### Module Collections

It can be a pain to have to enter a long list of module load commands every time you log on to the cluster. Module collections allow you to create saved environments that remember a set list of modules to load together. This method is particularly useful if you have two or more module sets that may conflict with one another.

To create a saved environment, simply load all of your desired modules and then type

``` bash
module save
```

This will save this set of modules as your default set. To save a set as a non-default, just assign the environment a name:

``` bash
module save environment_name
```

To load all the modules in the set, enter

``` bash
module restore
```

``` bash
module restore environment_name
```

to load the default or specified environment, respectively. To modify an environment, restore the environment, make the desired changes by loading and/or unloading modules and save it to the same name. To get a list of your environments, run:

``` bash
module savelist
```

## More Information

You can view documentation while on the cluster using the command:

``` bash
man module
```

There is even more information at the [offical lmod website](http://www.tacc.utexas.edu/tacc-projects/lmod).
