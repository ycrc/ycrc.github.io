#!/usr/bin/env python
import re
import sys
from collections import defaultdict
from itertools import product
from subprocess import check_output

## Globals ##

# GPU memory dict
vram_dict = {
    "k80": "12",
    "gtx1080ti": "11",
    "titanv": "12",
    "p100": "16",
    "v100": "16",
    "a100": "40",
    "a100-80g": "80",
    "a40": "48",
    "a5000": "24",
    "rtx2080": "8",
    "rtx2080ti": "11",
    "rtx3090": "24",
    "rtx4000": "8",
    "rtx5000": "16",
    "rtx8000": "48",
}

# Commons partitions, their display order
commons = {
    "general*": "Use the general partition for most batch jobs. This is the default if you don't specify one with `--partition`.",
    "day*": "Use the day partition for most batch jobs. This is the default if you don't specify one with `--partition`.",
    "interactive": "Use the interactive partition to jobs with which you need ongoing interaction. For example, exploratory analyses or debugging compilation.",
    "devel": "Use the devel partition to jobs with which you need ongoing interaction. For example, exploratory analyses or debugging compilation.",
    "week": "Use the week partition for jobs that need a longer runtime than day allows.",
    "transfer": "Use the transfer partition to stage data for your jobs to and from [cluster storage](/clusters-at-yale/data/#staging-data).",
    "gpu": "Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gpus` option in order to use them. For example, `--gpus=gtx1080ti:2` would request 2 GeForce GTX 1080Ti GPUs per node.",
    "gpu_devel": "Use the gpu_devel partition to debug jobs that make use of GPUs, or to develop GPU-enabled code.",
    "bigmem": "Use the bigmem partition for jobs that have memory requirements other partitions can't handle.",
    "mpi": "Use the mpi partition for tightly-coupled parallel programs that make efficient use of multiple nodes. See our [MPI documentation](/clusters-at-yale/job-scheduling/mpi) if your workload fits this description.",
    "scavenge": "Use the scavenge partition to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).",
    "scavenge_gpu": "Use the scavenge_gpu partition to run preemptable jobs on more GPU resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).",
}

# look for MemSpecLimit in slurm node config
mem_spec_limit = 6 #GiB
cpu_regex = re.compile(r"^.*,(E?\d-?\d+_?v?\d?r?)")
gres_regex = re.compile(r"gpu:([a-z0-9]+):(\d+)")
sinfo_cols = ["partition", "nodes", "cpus", "memory", "gres", "features"]
out_cols = ["Count", "CPU Type", "CPUs/Node", "Memory/Node (GiB)", "Node Features"]
out_cols_gpu = out_cols[:4] + ["GPU Type", "GPUs/Node", "vRAM/GPU (GB)"] + out_cols[4:]
tres_translate = {
    "cpu": "Maximum CPUs",
    "mem": "Maximum memory",
    "node": "Maximum nodes",
    "gres/gpu": "Maximum GPUs",
}

## Functions ##

def get_cluster_name():
    cluster = ""
    with open("/etc/yalehpc", "r") as hpcenv:
        for line in hpcenv:
            if line.startswith("export cluster"):
                cluster = line.split("=")[1].strip(' \n"')
                return cluster
    if cluster == "":
        sys.exit(1, "Couldn't find /etc/yalehpc, exiting.")

def get_part_hardware():

    """
    Example sinfo output
    bigmem|2|32|1543168|(null)|haswell,avx2,E7-4809_v3,nogpu
    bigmem|3|36|1543168|(null)|cascadelake,avx2,avx512,6240,nogpu
    general*|87|20|123904|(null)|haswell,avx2,E5-2660_v3,nogpu,standard,oldest
    general*|18|36|187392|(null)|cascadelake,avx2,avx512,6240,nogpu,standard
    gpu|1|8|123904|gpu:gtx1080ti:4|broadwell,avx2,E5-2637_v4,singleprecision
    gpu|2|20|123904|gpu:k80:4(S:0-1)|haswell,avx2,E5-2660_v3,doubleprecision
    gpu|8|8|123904|gpu:gtx1080ti:4(S:0-1)|broadwell,avx2,E5-2637_v4,singleprecision
    """
    part_hardware = defaultdict(lambda: [])
    parts_with_gpus = set()
    for part_line in check_output(
        ["sinfo", "--noheader", "-eo", "%P|%D|%c|%m|%G|%b"], universal_newlines=True
    ).split("\n"):
        line_dict = dict(zip(sinfo_cols, part_line.split("|")))
        if line_dict["partition"] != "":
            if line_dict["cpus"] == "0":
                continue
            partition_name = line_dict["partition"]
            mem = int(line_dict["memory"]) / 1024
            cpu_type = cpu_regex.match(line_dict["features"]).groups()[0]
            gpu_type = []
            gpu_mem = []
            gpu_num = []
            
            if line_dict["gres"] != "(null)":
                parts_with_gpus.add(line_dict["partition"])
                for gpu, num in gres_regex.findall(line_dict["gres"]):
                    gpu_type.append(gpu)
                    gpu_num.append(num)
                    gpu_mem.append(vram_dict[gpu])
            table_dict = dict(
                zip(
                    out_cols_gpu,
                    [
                        line_dict["nodes"],
                        cpu_type,
                        line_dict["cpus"],
                        f"{mem:0.0f}",
                        ",".join(gpu_type),
                        ",".join(gpu_num),
                        ",".join(gpu_mem),
                        ", ".join(line_dict["features"].split(",")),
                    ],
                )
            )

            part_hardware[partition_name].append(table_dict)
    return part_hardware, parts_with_gpus


def tres_to_english(tres_type, tres_string):
    english = []
    per = ""

    if tres_type.endswith("U"):
        per = " per user"
    elif tres_type.endswith("A"):
        per = " per group"
    elif tres_type == "GrpTRES":
        per = " in use"
    else:
        per = " per job"

    if tres_type.startswith("MaxJobs"):
        limit_name = "Maximum running jobs" + per
        english.append([limit_name, tres_string])
    elif tres_type.startswith("MaxSubmit"):
        limit_name = "Maximum submitted jobs" + per
        english.append([limit_name, tres_string])
    else:
        tres = dict([x.split("=") for x in tres_string.split(",")])
        for lim in tres:
            limit_name = tres_translate[lim] + per
            english.append([limit_name, tres[lim]])
    return english


def defaults_to_args(defaults):
    default_slurm_args = (
        f'--time={defaults["DefaultTime"]} --nodes=1 --ntasks=1 --cpus-per-task=1'
    )
    if defaults["OverSubscribe"] == "EXCLUSIVE":
        default_slurm_args += " --exclusive"
    if "DefMemPerCPU" in defaults:
        default_slurm_args += f' --mem-per-cpu={defaults["DefMemPerCPU"]}'
    elif "DefMemPerNode" in defaults:
        default_slurm_args += f' --mem={defaults["DefMemPerNode"]}'
    return default_slurm_args


def get_defaults_and_limits(part_hardware):
    limits = dict()
    defaults = defaultdict(lambda: dict())
    for partition in part_hardware:
        scont_dict = dict()
        english_limits = []
        scont = check_output(
            ["scontrol", "-o", "show", "part", partition.rstrip("*")],
            universal_newlines=True,
        ).split()
        scont_dict = dict([x.split("=", 1) for x in scont])
        defaults[partition] = defaults_to_args(scont_dict)

        sacct = check_output(
            ["sacctmgr", "-p", "show", "qos", scont_dict["QoS"]],
            universal_newlines=True,
        ).split("\n")
        sacct_dict = dict(zip(sacct[0].split("|"), sacct[1].split("|")))
        limit_names = [
            "".join(x)
            for x in list(product(["MaxTRES", "MaxJobs", "MaxSubmit"], ["PA", "PU"]))
            + ["MaxTRES", "GrpTRES"]
        ]
        for limit in ["MaxWall"] + limit_names:
            if limit in sacct_dict:
                scont_dict[limit] = sacct_dict[limit]
            else:
                scont_dict[limit] = ""
        if scont_dict["MaxTime"] == "UNLIMITED":
            if scont_dict["MaxWall"] != "":
                english_limits.append(["Maximum job time limit", scont_dict["MaxWall"]])
        else:
            english_limits.append(["Maximum job time limit", scont_dict["MaxTime"]])
        for tres in limit_names:
            if scont_dict[tres] != "":
                english_limits += tres_to_english(tres, scont_dict[tres])
        limits[partition] = english_limits
    return defaults, limits


def iprint(i, toprint):
    indent = "    " * i
    print(indent + toprint)


def collapse_memory_differences(partition_hardware, has_gpus):

    nodes_by_features = defaultdict(lambda: [])
    # group by features
    for node_type in partition_hardware:
        features = node_type["Node Features"]
        if has_gpus:
            features = f"features, {node_type['GPU Type']}, {node_type['GPUs/Node']}"
        nodes_by_features[features].append(node_type)

    collapsed_partition_hardware = []
    #find minimum reported memory for similar node type
    for similar_nodes in nodes_by_features.values():

        memory_bins = {}
        for node_subtype in similar_nodes:
            memory = node_subtype["Memory/Node (GiB)"]

            if len(memory_bins) == 0:
                memory_bins = {memory: [node_subtype]}
            else:
                new_bin = True
                for memory_bin in memory_bins:
                    #if the difference is less that 2GiB, add nodes to list
                    if abs(int(memory) - int(memory_bin)) < 2:
                        memory_bins[memory_bin].append(node_subtype)
                        # replace key with new minimum
                        if int(memory) < int(memory_bin):
                            memory_bins[memory] = memory_bins.pop(memory_bin)
                        new_bin = False
                        break
                if new_bin:
                    memory_bins[memory] = [node_subtype]

        for min_memory, similar_nodes in memory_bins.items():
            new_count = 0
            for node_subtype in similar_nodes:
                new_count += int(node_subtype['Count'])

            # override node type with new count and memory
            collapsed_node_type = similar_nodes[0]
            collapsed_node_type["Count"] = str(new_count)
            collapsed_node_type["Memory/Node (GiB)"] = min_memory
            collapsed_partition_hardware.append(collapsed_node_type)

    return collapsed_partition_hardware


def sort_hardware(partition_hardware):


    node_gens = ["icelake", "cascadelake", "skylake", "broadwell", "haswell", "epyc", "milan"]
    nodes_by_gen = {}

    for node_type in partition_hardware:

        for feature in node_type["Node Features"].split(", "):
            if feature in node_gens:
                node_gen = feature
                break

        if node_gen not in nodes_by_gen.keys():
            nodes_by_gen[node_gen] = []

        if "standard" in node_type["Node Features"]:
            nodes_by_gen[node_gen].insert(0, node_type)
        else:
            nodes_by_gen[node_gen].append(node_type)

    sorted_hardware = []
    for gen in node_gens:
        if gen in nodes_by_gen.keys():
            sorted_hardware += nodes_by_gen[gen]

    return sorted_hardware


def print_part_table(i, partition, hardware_list, has_gpus, defaults, limits):
    if has_gpus:
        cols = out_cols_gpu
    else:
        cols = out_cols

    partition_displayname = partition

    iprint(0 + i, f'=== "{partition_displayname.rstrip("*")}"\n')
    if partition in commons:
        iprint(1 + i, commons[partition] + "\n")
    iprint(1 + i, "**Request Defaults**\n")
    iprint(
        1 + i,
        f"Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.\n",
    )
    iprint(1 + i, "``` text")
    iprint(1 + i, defaults)
    iprint(1 + i, "```\n")
    if has_gpus:
        iprint(1 + i, '!!! warning "GPU jobs need GPUs!"')
        iprint(
            2 + i,
            "Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.",
        )

    if len(limits) > 0:
        iprint(1 + i, "**Job Limits**\n")
        iprint(
            1 + i,
            f"Jobs submitted to the {partition.rstrip('*')} partition are subject to the following limits:\n",
        )
        iprint(1 + i, "|Limit|Value|")
        iprint(1 + i, "|---|---|")
        for limit, value in limits:
            iprint(1 + i, f"|{limit}|`{value}`|")
        print("")
    iprint(1 + i, "**Available Compute Nodes**\n")
    iprint(
        1 + i,
        "Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.\n",
    )
    iprint(1 + i, "|" + "|".join(cols) + "|")
    iprint(1 + i, "|" + "|".join(["---"] * len(cols)) + "|")

# this isn't working as intended, but its not currently needed.
  #  part_hardware[partition] = collapse_memory_differences(part_hardware[partition], has_gpus)

    for line in sort_hardware(part_hardware[partition]):
        iprint(1 + i, "|" + "|".join([line[col] for col in cols]) + "|")

    print("")



cluster_name = get_cluster_name()

part_hardware, parts_with_gpus = get_part_hardware()
defaults, limits = get_defaults_and_limits(part_hardware)
for part in commons:
    if part in part_hardware:
        print_part_table(
            0,
            part,
            part_hardware[part],
            part in parts_with_gpus,
            defaults[part],
            limits[part],
        )

pi_parts = [
    part
    for part in part_hardware
    if (part.startswith("pi_") or part.startswith("psych_"))
]

ycga_parts = [
    part
    for part in part_hardware
    if part.startswith("ycga")
]

if len(pi_parts) > 0:
    print("### Private Partitions")
    print(
        "With few exceptions, jobs submitted to private partitions are not considered when calculating your group's [Fairshare](/clusters-at-yale/job-scheduling/fairshare/). Your group can purchase additional hardware for private use, which we will make available as a `pi_groupname` partition. These nodes are purchased by you, but supported and administered by us. After vendor support expires, we retire compute nodes. Compute nodes can range from $10K to upwards of $50K depending on your requirements. If you are interested in purchasing nodes for your group, please [contact us](/#get-help).\n"
    )
    print('??? summary "PI Partitions (click to expand)"')
    for part in sorted(pi_parts):
        print_part_table(
            1,
            part,
            part_hardware[part],
            part in parts_with_gpus,
            defaults[part],
            limits[part],
        )

if len(ycga_parts) > 0:
    print("### YCGA Partitions")
    print(
        "The following partitions are intended for projects related to the [Yale Center for Genome Analysis](http://ycga.yale.edu/). Please do not use these partitions for other proejcts. Access is granted on a group basis. If you need access to these partitions, please [contact us](/#get-help) to get approved and added.\n"
    )
    print('??? summary "YCGA Partitions (click to expand)"')
    for part in sorted(ycga_parts):
        print_part_table(
            1,
            part,
            part_hardware[part],
            part in parts_with_gpus,
            defaults[part],
            limits[part],
        )
