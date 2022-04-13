# Passing values into batch jobs

A useful tool when running jobs on the clusters is to be able to pass variables into a script without modifying any code.
This can include specifying the name of a data file to be processed, or setting a variable to a specific value.
Generally, there are two ways of achieving this: environment variables and command-line arguments.
Here we will work through how to implement these two approaches in both Python and R.

## Python

### Environment variables

In python, environment variables are accessed via the `os` package ([docs page](https://docs.python.org/3/library/os.html)).
In particular, we can use `os.getenv` to retrieve environment variables set prior to launching the python script.

For example, consider a python script designed to process a data file:

```Python
def file_cruncher(file_name):

    f = open(file_name)
    data = f.read()
    output = process(data)
    # processing code goes here
    return output
```


We can use an environment variable (`INPUT_DATA_FILE`) to provide the filename of the data to be processed.
The python script (`my_script.py`) is modified to retrieve this variable and analyze the given datafile:

```Python
import os

file_name = os.getenv("INPUT_DATA_FILE")

def file_cruncher(file_name):

    f = open(file_name)
    data = f.read()
    output = process(data)
    # processing code goes here
    return output
```

To process this data file, you would simply run:

```bash
export INPUT_DATA_FILE=/path/to/file/input_0.dat
python my_script.py
```

This avoids having to modify the python script to change which datafile is processed, we only need to change the environment variable.

### Command-line arguments

Similarly, one can use command-line arguments to pass values into a script.
In python, there are two main packages designed for handling arguments.
First is the simple `sys.argv` function which parses command-line arguments into a list of strings:

```Python
import sys

for a in sys.argv:
    print(a)
```

Running this with a few arguments:

```bash
$ python my_script.py a b c
my_script.py
a
b
c
```
The first element in `sys.argv` is the name of the script, and then all subsequent arguments follow.

Secondly, there is the more fully-featured `argparse` package ([docs page](https://docs.python.org/3/library/argparse.html))which offers many advanced tools to manage command-line arguments.
Take a look at their documentation for examples of how to use `argparse`.

## R

Just as with Python, R provides comparable utilities to access command-line arguments and environment variables.

### Environment variables

The `Sys.getenv` utility ([docs page](https://rdocumentation.org/packages/base/versions/3.6.2/topics/Sys.getenv)) works nearly identically to the Python implementation.

```R
> Sys.getenv('HOSTNAME')
[1] "grace2.grace.hpc.yale.internal"
```

Just like Python, these values are always returned as `string` representations, so if the variable of interest is a number it will need to be cast into an integer using `as.numeric()`.

### Command-line arguments

To collect command-line arguments in R use the `commandArgs` function:

```R
args = commandArgs(trailingOnly=TRUE)

for (x in args){
   print(x)
}
```

The `trailingOnly=TRUE` option will limit `args` to contain only those arguments which follow the script:

```bash
Rscript my_script.R a b c
[1] "a"
[1] "b"
[1] "c"
```

There is a more advanced and detailed package for managing command-line arguments called `optparse` ([docs page](https://cran.r-project.org/web/packages/optparse/)).
This can be used to create more featured scripts in a similar way to Python's `argparse`.

## Slurm environment variables

Slurm sets a number of environment variables detailing the layout of every job.
These include:

- `SLURM_JOB_ID`: the unique jobid given to each job. Useful to set unique output directories
- `SLURM_CPUS_PER_TASK`: the number of CPUs allocated for each task. Useful as a replacement for R's `detectCores` or Python's `multiprocessing.cpu_count` which report the physical number of CPUs and not the number allocated by Slurm.
- `SLURM_ARRAY_TASK_ID`: the unique array index for each element of a job array. Useful to un-roll a loop or to set a unique random seed for parallel simulations.

These can be leveraged within batch scripts using the above techniques to either pass on the command-line or directly reading the environment variable to control how a script runs.

For example, if a script previously looped over values ranging from 0-9, we can modify the script and create a job array which runs each iteration separately in parallel using `SLURM_ARRAY_TASK_ID` to tell each element of the job array which value to use.
