#Compile MATLAB program

By compiling your MATLAB code into standalone executables, you eliminate the need to load the MATLAB module each time you run the code. This can be particularly beneficial on clusters where loading the MATLAB module involve loading all the installed packages and can be time-consuming. This can reduce the startup time and improve the overall performance of executing the code. If you choose to compile your MATLAB code into standalone executables, one disadvantage is that every time you make changes to your program, you will need to recompile it. Recompiling is necessary to ensure that any modifications or updates you’ve made to the code are incorporated into the executable. 
 
## Compile MATLAB 

When compiling MATLAB code, the compilation process generates several additional files. To maintain organization in your current directory, it is recommended to create a new directory specifically for the compiled files.

For example, to compile function1.m, function2.m, and function3.m, where function1.m is the main MATLAB function you call: 

```
mkdir compiled_scripts
cd compiled_scripts
salloc 
module load MATLAB/2022b
mcc -m function1 function2 function3
```

This will generate multiple files, including the executable named  `function1`. Please note that there are [functions that are not supported by MATLAB compiler](https://www.mathworks.com/help/compiler/unsupported-functions.html).

## Run the Executable

Load the MATLAB Runtime and GCCcore modules to run the executable. Always ensure that you load the same version of the MATLAB Runtime as the version of MATLAB you used for compilation.

```
module load MCR/R2022b.5 GCCCore 
./function1 <argument_list> 
```

The argument list is the list of input parameters for function1.m.

## Job Arrays

If you are running a large number of jobs with job arrays, we recommend setting up a unique directory for each job to use as a cache location. You can use the /tmp space on the compute node. Here is an example of a batch script:

```
#!/bin/bash
#SBATCH --job-name myjob
#SBATCH --array 1-100
#SBATCH --mem 5G
#SBATCH -t 1:00:00

mcr_cache_root=/tmp/$USER/MCR_CACHE_ROOT_${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}
mkdir -p $mcr_cache_root
export MCR_CACHE_ROOT=$mcr_cache_root

module load MCR/2022b.5 GCCcore 
./function1.sh ${SLURM_ARRAY_TASK_ID}
```





