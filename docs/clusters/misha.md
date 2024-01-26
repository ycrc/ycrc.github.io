# Misha

![Misha](/img/misha.jpeg){: .cluster-portrait}

Misha is a cluster intended for use on projects associated with the [Wu Tsai Institute](https://wti.yale.edu/), an interdisciplinary research endeavor at Yale University connecting neuroscience and data science to accelerate breakthroughs in understanding cognition. 

Misha is named for [Dr. Misha Mahowald](https://en.wikipedia.org/wiki/Misha_Mahowald), an American computational neuroscientist in the neuromorphic engineering, known for her work on the silicon retina. 

- - -

!!! info "Beta"
    Misha is currently in closed beta. For access, please contact Ping Luo (ping.luo@yale.edu). 

## Access the Cluster

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed [via ssh](/clusters-at-yale/access) or through the [Open OnDemand web portal](/clusters-at-yale/access/ood/).


## System Status and Monitoring

For system status messages and the schedule for upcoming maintenance, please see the [system status page](https://research.computing.yale.edu/support/hpc/system-status). For a current node-level view of job activity, see the [cluster monitor page (VPN only)](http://cluster.ycrc.yale.edu/milgram/).

## Partitions and Hardware

Misha is made up of several kinds of compute nodes. We group them into  (sometimes overlapping) [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. By combining the `--partition` and [`--constraint`](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) Slurm options you can more finely control what nodes your jobs can run on.

--8<-- "snippets/submission_rate_limit.md"


### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/misha_partitions.md"
