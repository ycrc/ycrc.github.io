# GPU Monitoring with Jobstats

Jobstats is the primary mechanism for evaluating GPU/CPU usage on Yale Research Computing systems. It can display usage in two formats:

- a text summary of a specific job within a terminal
- a graphical summary of usage/time for a specific job

Jobstats provides live reporting of GPU/CPU usage, so you can monitor your job as it runs. 

This page will cover how to interpret your Jobstats outputs for various GPU utilizations so as to highlight potential areas for optimization in your workflow. For instructions on running Jobstats, see [Jobstats](../../clusters-at-yale/job-scheduling/jobstats.md).

## Metrics relevant to AI workloads

Relevant metrics include:

- GPU utilization (Total amount of the GPU's computing power you are using)
- GPU memory usage (total vRAM used, note: This is separate from --mem in Slurm)
- CPU utilization (for loading data and other non-GPU workflows)
- Wall time (How long your job is running)

## Jobstats considerations

All GPU nodes provide access to many GPUs on a single node.

Common observations:
- only one GPU shows memory usage (issue with multi-GPU setup)
- low average utilization across devices (not loading enough data on GPU)
- uneven memory distribution 

These patterns typically indicate misconfigured device placement.

## Common Jobstats patterns

| Observation | Likely interpretation |
|------------|----------------------|
| low memory, low utilization | Batch size too small |
| One GPU active | Multi-GPU misconfiguration |
| long periods of GPU inactivity | Data loading bottleneck |
| High CPU, low GPU | Model running on CPU/issue with pytorch/tensorflow installation |

Below are visual representations of common issues with GPU workflows:

## Example: CPU bottleneck with data loading - Coming soon!

<!--
![Single GPU Jobstats example](assets/ai/jobstats/single_gpu_example.png)
-->

## Example: multi-GPU misconfiguration - Coming soon!

<!--
![Multi-GPU Jobstats example](assets/ai/jobstats/multigpu_one_active.png)
-->

## Using Jobstats to Scale workflows

- Start with one GPU and confirm usage. Identify total GPU utilization and memory usage with Jobstats
- Try tinkering with the amount of data loaded, CPU totals, etc to see how utilization and memory usage changes
- If using entire GPU, try multiple GPUs on same node (will require code modification) and confirm with Jobstats
     - Note: You shouldn't need to modify batch size as it was already optimized for one GPU
- For complex workflows with multinode GPUs, see [multinode GPU jobs](miniconda-multigpu.md)

## Jobstats killed my job!

As of 2026, Jobstats will kill jobs that aren't using GPUs effectively (<10% usage). This is to ensure that GPUs, a limited and competitive resource,
 is available to researchers that will benefit from the computing power GPUs provide. 
If you are having issues with Jobstats killing your jobs, please reach out to research.computing@yale.edu and we will be happy to help.
