# Job Performance Monitoring

We have recently deployed a new tool for measuring and monitoring job performance called [`jobstats`](https://github.com/ycrc/jobstats). 
Available on all clusters, `jobstats` provides a report of the utilization of CPU, Memory, and GPU resources for in-progress and recently completed jobs. 
To generate the report simply run (replacing the ID number of the job in question):

```
[ab123@login1.bouchet ~]$ jobstats 123456789
================================================================================
                              Slurm Job Statistics
================================================================================
         Job ID: 123456789
   User/Account: ab123/group
       Job Name: gpu_job
          State: COMPLETED
          Nodes: 1
      CPU Cores: 4
     CPU Memory: 32GB (8GB per CPU-core)
           GPUs: 1
  QOS/Partition: normal/gpu
        Cluster: bouchet
     Start Time: Mon Aug 10, 2026 at 12:01 AM
       Run Time: 00:04:57
     Time Limit: 02:00:00

                              Overall Utilization
================================================================================
  CPU utilization  [|||||||||||||                                  27%]
  CPU memory usage [|                                               3%]
  GPU utilization  [||||||||||||||||||||||||||||||||||||||         77%]
  GPU memory usage [|||||||||||||||||||||||||||||||||              66%]

                              Detailed Utilization
================================================================================
  CPU utilization per node (CPU time used/run time)
      a1128u14n01: 00:05:20/00:19:48 (efficiency=27.0%)

  CPU memory usage per node - used/allocated
      a1128u14n01: 872.1MB/32GB (218.0MB/8GB per core of 4)

  GPU utilization per node
      a1128u14n01 (GPU 3): 77%

  GPU memory usage per node - maximum used/total
      a1128u14n01 (GPU 3): 21.2GB/32GB (66.3%)

                                     Notes
================================================================================
  * To view a graphical report of this job's performance, see:
      https://ood-bouchet.ycrc.yale.edu/pun/sys/ycrc_userportal/jobefficiency/123456789
    Have a nice day!
```

When viewed from our [User portal graphical interface](https://docs.ycrc.yale.edu/clusters-at-yale/access/ood/#user-portal), these statistics are enhanced with plots of performance over time.

![jobstats web](/img/ood_jobstats.jpg)

This is a great way to monitor your job's behavior and resource utilization over time. 
