# Parallel

[GNU Parallel](https://www.gnu.org/software/parallel/) a simple but powerful way to run independent tasks in parallel.  Although it is possible to run on multiple nodes, it is simplest to run on multiple cpus of a single node, and that is what we will consider here.  Note that what is presented here just scratches the surface of what parallel can do.

## Basic Examples

### Loop

Let's parallelize the following bash loop that prints the letters `a` through `f` using bash's [brace expansion](https://www.gnu.org/software/bash/manual/bashref.html#Brace-Expansion):

``` bash
for letter in {a..f};
do
    echo $letter
done
```

... which produces the following output:

``` bash
a
b
c
d
e
f
```

To achieve the same result, `parallel` starts some number of workers and then runs tasks on them.  The number of workers and tasks need not be the same. You specify the number of workers with `-j`. The tasks can be generated with a list of arguments specified after the separator `:::`. For parallel to perform well, you should allocate at least the same number of CPUs as workers with the Slurm option `--cpus-per-task` or more simply `-c`.

``` bash
salloc -c 4
module load parallel
parallel -j 4 "echo {}" ::: {a..f}
```

This runs four workers that each run `echo`, filling in the argument `{}` with the next item in the list. This produces the output:

### Nested Loop

Let's parallelize the following nested bash loop.

``` bash
for letter in {a..c}
do
    for number in {1..7..2}
    do
        echo $letter $number
    done
done
```

... which produces the following output:

``` bash
a 1
a 2
a 3
b 1
b 2
b 3
c 1
c 2
c 3
```

You can use the `:::` separator with `parallel` to specify multiple lists of parameters you would like to iterate over. Then you can refer to them by one-based index, e.g. list one is `{1}`. Using these, you can ask parallel to execute combinations of parameters. Here is a way to recreate the result of the serial bash loop above:

``` bash
parallel -j 4 "echo {1} {2}" ::: {a..c} ::: {1..3}
```

## Advanced Examples

### `md5sum`

You have a number of files scattered throughout a directory tree.  Their names end with fastq.gz, e.g. d1/d3/sample3.fastq.gz.  You'd like to run md5sum on each, and put the output in a file in the same directory, with a filename ending with .md5sum, e.g. d1/d3/sample3.md5sum.
Here is a script that will do that in parallel, using 16 cpus on one node of the cluster:

``` bash
#!/bin/bash
#SBATCH -c 16

module load parallel
parallel -j ${SLURM_CPUS_PER_TASK} --plus "echo {}; md5sum {} > {/fastq.gz/md5sum.new}" ::: $(find . -name "*.fastq.gz" -print)
```

The `$(find . -name "*.fastq.gz" -print)` portion of the command returns all of the files of interest. They will be plugged into the {} in the md5sum command. `{/fastq.gz/md5sum.new}` does a string replacement on the filename, producing the desired output filename.  String
replacement requires the --plus flag to parallel, which enables a number of powerful string manipulation features. Finally, we pass `-j ${SLURM_CPUS_PER_TASK}` so that parallel will use all of the allocated cpus, however many there are.

### Parameter Sweep

You want to run a simulation program that takes a number of input parameters, and you want to sample a variety of values for each parameter.

``` bash
#!/bin/bash
#SBATCH -c 16
module load parallel
parallel -j ${SLURM_CPUS_PER_TASK} simulate {1} {2} {3} ::: {1..5} ::: 2 16 ::: {5..50..5}
```

This will run 100 jobs, each with parameters that vary as :

``` bash
simulate 1 2 5
simulate 1 2 10
simulate 1 2 15
...
simulate 5 16 45
simulate 5 16 50
```

If `simulate` doesn't create unique output based on parameters, you can use redirection so you can review results from each task. You'll need to use quotes so that the > is seen as part of the command:

``` bash
parallel -j ${SLURM_CPUS_PER_TASK} "simulate {1} {2} {3} > results_{1}_{2}_{3}.out" ::: $(seq 1 5) ::: 2 16 ::: $(seq 5 5 50)
```
