
# ClusterShell

[ClusterShell](https://clustershell.readthedocs.io/en/latest/intro.html) is a useful Python package for executing arbitrary commands across multiple hosts. On the Yale clusters it provides a relatively simple way for you to run commands on nodes your jobs are running on, and collect the results. The two most useful commands provided are [`nodeset`](#nodeset), which can show and manipulate node lists and [`clush`](#clush), which can run commands on multiple nodes at once.

## Configuration

To set up ClusterShell, make sure you have a `.config` directory and a copy our [`groups.conf`](/_static/files/clustershell_groups.conf) file there. For more info about ClusterShell configuration for Slurm, see [the official docs](https://clustershell.readthedocs.io/en/latest/config.html#slurm-group-bindings).

``` bash
mkdir -p ~/.config/clustershell
wget https://docs.ycrc.yale.edu/_static/files/clustershell_groups.conf -O ~/.config/clustershell/groups.conf 
```

We provide ClusterShell as a module, but you can also install it with `conda`.

#### Module

``` bash
module load ClusterShell
```

#### Conda

``` bash
module load miniconda
conda create -yn clustershell python pip
source activate clustershell
pip install ClusterShell
```

## Examples

### `nodeset`

The [`nodeset`](https://clustershell.readthedocs.io/en/latest/tools/nodeset.html#nodeset-tool) command uses `sinfo` underneath but has slightly different syntax. You can use it to ask about node states and nodes your job is running on. The nice difference is you can ask for folded (e.g. `c[01-02]n[12,15,18]`) or expanded (e.g. `c01n01 c01n02 ...`) node lists. The groups useful to you that we have configured are `@user`, `@job` and `@state`.

#### User group

List expanded node names where user abc123 has jobs running

``` bash
# similar to squeue -h -u abc123 -o "%N"
nodeset -e @user:abc123
```

#### Job group

List folded nodes where job 1234567 is running

``` bash
# similar to squeue -h -j 1234567 -o "%N"
nodeset -f @job:1234567
```

#### State group

List expanded node names that are idle according to Slurm

``` bash
# similar to sinfo -t IDLE -o "%N"
nodeset -e @state:idle
```

### `clush`

The [`clush`](https://clustershell.readthedocs.io/en/latest/tools/clush.html) command uses the node grouping syntax from nodeset to allow you to run commands on those nodes. `clush` uses ssh to connect to each of these nodes. You can use the `-b` option to gather output from nodes with same output into the same lines. Leaving this out will report on each node separately.

!!! info
    You can only ssh to, and therefore run `clush` on, nodes where you have active jobs.

#### Local storage

Get a list of files in /tmp/abs on all nodes where job `654321` is running.

``` bash
clush -bw @job:654321 ls /tmp/abc123

# don't gather identical output
clush -w @job:654321 ls /tmp/abc123
```

#### CPU usage

Show %cpu, memory usage, and command for all nodes running any jobs owned by user `abc123`.

``` bash
clush -bw @user:abc123 ps -uabc123 -o%cpu,rss,cmd
```

#### GPU usage

Show what's running on all the GPUs on the nodes associated with your job `654321`.

``` bash
clush -bw @job:654321 nvidia-smi --format=csv --query-compute-apps=process_name,used_gpu_memory
```
