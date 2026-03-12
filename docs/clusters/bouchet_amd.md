# Bouchet AMD nodes

YCRC has added additional compute nodes to the Bouchet HPC cluster. YCRC has historically deployed Intel-based compute nodes. All the new nodes, however, will utilize AMD processors for the first time in YCRC clusters. We have added 26 CPU-only nodes with 128-core AMD EPYC 9575F Processors, and 8 nodes with 128-core AMD EPYC 9575F processors and 8 NVIDIA RTX Pro 6000 Blackwell Server Edition GPU cards per node. Both Intel and AMD processors use the x86-64 instruction set, but there are architectual differences that can impact the software compilation process and application performance. 


## Partitions

The CPU-only AMD nodes are in the `day_amd` partition, and the GPU AMD nodes are in the `gpu_amd` parition. 

For detailed information about job limits and available compute nodes in each
partition, please refer to [our Bouchet partition documentation](/clusters/bouchet/#partitions-and-hardware).


## Software modules

We have recompiled most software modules with compilation flags that enabled them to run on both Intel and AMD nodes. If you are running any software compiled with CUDA on the RTX Pro 6000 Blackwell Server Edition GPUs, please use the modules installed with CUDA 12.8.0. Software built with older CUDA versions may fail or result inpoorer performance. If you see any missing modules or experience issues with software modules, please [reach out to us](/).   


## Compiling your code

If you compile your code optimized for Intel node architecture, it will not run on AMD nodes, and vice versa. To run your code on both Intel and AMD nodes, you need to compile it with a compiler flag that specifies a compatible instruction set. You can compile your code on either types of compute node. 

If you are building your code with GCC, please include the compiler flag `--march=x86-64-v4`. If you are using Intel compilers, we recommend compiling and running your workflow on the Intel nodes. If you would still like to run the code on AMD nodes, please compile it with the compiler flag `-axCORE-AVX512`.

If you would like to compile your code optimized for a specific node architecture, please request an intereactive compute sesssion on that architecture (`devel` for Intel nodes and `day_amd` for AMD nodes) and compile your code with `--martch=native` for GCC and `-xHost` for Intel compilers. Please run your code only on the same architecutre on which it was compiled. 

If you need any assistance compiling your code, please [reach out to us](/).  

## Report Issues

If you discover issues when running your workflow or experience performance issues, feel free to [contact](/) us for assistance. 
Please include the working directory, the commands that were run, the software modules used, and any more information needed to reproduce the issue.






  
