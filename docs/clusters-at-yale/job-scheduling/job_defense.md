# Automated Detection of Idle Resources

The resources that power our computing systems are expensive to procure, operate, and maintain.
Allocated resources that are not used efficiently reduce available computing to all members of the YCRC community and degrade the overall computing experience.
In particular, idle GPUs are particularly damaging due to their limited number, large demand, and high operating cost. 
In the past, we have manually searched for jobs with idle resources and cancelled them to enable other researchers to use these GPUs. 
However, the growing number of GPUs has made this challening to enforce uniformly. 
In accordance to our [Cluster Usage Policies](/clusters-at-yale/policies), we have now implemented automations that detect idle resources and manages notifications and cancellations. 
This ensures that resources are not wasted and works to reduce wait times for pending jobs, thereby improving everyone's experience. 

## Idle GPU jobs

This daemon currently is configured to look at jobs running in Bouchet's non-interactive GPU partitions (`gpu`, `gpu_h200`, `priority_gpu`, and `scavenge_gpu`). 
We have two criteria:

1. Jobs which never use the GPU at all
2. Jobs which use a GPU for some of the job, but then leave the GPUs idle for long periods of time

For the former, we have implemented a warning email notification when a job has been runing for 30 minutes without using a GPU at all. 
After 1 hour, another email is sent out and the job is cancelled. 

For the second type of jobs, the warning is sent out after 1 hour of GPU idleness anywhere in the job, with cancellation after 2 hours of idle GPUs. 

