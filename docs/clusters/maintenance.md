# Cluster Maintenance

Each YCRC cluster undergoes regular scheduled maintenance twice a year.
During the maintenance, the cluster is unavailable, logins are deactivated and all pending jobs are held. 
Unless otherwise stated, the storage for that cluster will also be inaccessible during the maintenance.
We use this opportunity when jobs are not running and there are no users on the machine to make upgrades and changes that would be disruptive. 
These activities include updating and patching the compute resources including the compute nodes, networking, service nodes and storage as well as making changes to critical infrastructure.

Each maintenance is scheduled for three days, from Tuesday morning through end of day Thursday of the respective week. 
In many cases, the cluster may return to service early and, under extenuating circumstances, we may choose to extend maintenance if necessary to make sure the system is stable before restoring access and jobs.

Communication will be sent to all users of the respective cluster both 4 weeks and 1 week prior to the maintenance period.

## Schedule

The schedule for the regular cluster maintenance is posted below. 
Please be mindful of these dates and schedule your work accordingly to avoid disruptions.

| Date            | Cluster  |
|-----------------|----------|
| Sept 24th       | Hopper  |
| Winter (TBD)    | Other clusters |     

Occasionally we will schedule additional maintenance periods beyond those listed above, and potentially with shorter notices, if urgent work arises, such as power work on the data center or critical upgrades for stability or security. 
We will give as much notice as possible in advance of these maintenance outages.

## Job Submission before Maintenance

As the maintenance window approaches, the Slurm scheduler will not start any job if the job’s requested wallclock time extends
past the start of the maintenance period. If you run squeue, such jobs will show as
pending jobs with the reason "ReqNodeNotAvail."  However, by reducing your job's requested wallclock time, you may be able to
run the job before the maintenance begins.

You can run the command "htnm" (short for "hours_to_next_maintenance") to determine the number of hours until the next maintenance
period.  Submit the job with a shorter time limit using "-t" or "--time".

Held jobs will automatically return to active status after the maintenance period, at which time they will run in normal
priority order.  All running jobs will be terminated at the start of the maintenance period.  Please plan accordingly.
