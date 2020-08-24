#!/usr/bin/env python
import re
import sys
from collections import defaultdict
from itertools import product
from subprocess import check_output

# Links for CPUs/GPUs

# GPU memory dict
vram_dict = {
    "k80": "12",
    "gtx1080ti": "11",
    "titanv": "12",
    "p100": "16",
    "v100": "16",
    "rtx2080": "8",
    "rtx2080ti": "11",
    "rtx4000": "8",
    "rtx5000": "16",
    "rtx8000": "48",
}
# Commons partitions, their display order
commons = {
    "general*": "Use the general partition for most batch jobs. This is the default if you don't specify one with `--partition`.",
    "day*": "Use the day partition for most batch jobs. This is the default if you don't specify one with `--partition`.",
    "short*": "Use the short partition for most batch jobs. This is the default if you don't specify one with `--partition`.",
    "interactive": "Use the interactive partition to jobs with which you need ongoing interaction. For example, exploratory analyses or debugging compilation.",
    "development": "Use the development partition for jobs where you are interactively developing code.",
    "education": "Use the education partition for course work.",
    "week": "Use the week partition for jobs that need a longer runtime than day allows.",
    "transfer": "Use the transfer partition to stage data for your jobs to and from [cluster storage](/clusters-at-yale/data/#staging-data).",
    "gpu": "Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gres` option in order to use them. For example, `--gres=gpu:gtx1080ti:2` would request 2 GeForce GTX 1080Ti GPUs per node.",
    "gpu_devel": "Use the gpu_devel partition to debug jobs that make use of GPUs, or to develop GPU-enabled code.",
    "bigmem": "Use the bigmem partition for jobs that have memory requirements other partitions can't handle.",
    "mpi": "Use the mpi partition for tightly-coupled parallel programs that make efficient use of multiple nodes. See our [MPI documentation](/clusters-at-yale/job-scheduling/mpi) if your workload fits this description.",
    "long": "Use the long partition for jobs that need a longer runtime than short allows.",
    "verylong": "Use the verylong partition for jobs that need a longer runtime than long allows.",
    "scavenge": "Use the scavenge partition to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).",
    "scavenge_gpu": "Use the scavenge_gpu partition to run preemptable jobs on more GPU resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).",
}

cpu_regex = re.compile(r"^.*,(E?\d-?\d+_?v?\d?)")
gres_regex = re.compile(r"gpu:([a-z0-9]+):(\d+)")
sinfo_cols = ["partition", "nodes", "cpus", "memory", "gres", "features"]
out_cols = ["Nodes", "CPU Type", "CPUs/Node", "Memory/Node (GiB)", "Node Features"]
out_cols_gpu = out_cols[:4] + ["GPU Type", "GPUs/Node", "vRAM/GPU (GB)"] + out_cols[4:]
tres_translate = {
    "cpu": "Maximum CPUs",
    "mem": "Maximum memory",
    "node": "Maximum nodes",
    "gres/gpu": "Maximum GPUs",
}


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
            part_hardware[line_dict["partition"]].append(table_dict)
    return part_hardware, parts_with_gpus


def tres_to_english(tres_type, tres_string):
    english = []
    per = ""

    if tres_type.endswith("U"):
        per = " per user"
    elif tres_type.endswith("A"):
        per = " per group"
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
            for x in product(["MaxTRES", "MaxJobs", "MaxSubmit"], ["PA", "PU"])
        ]
        for limit in ["MaxWall"] + limit_names:
            if limit in sacct_dict:
                scont_dict[limit] = sacct_dict[limit]
            else:
                scont_dict[limit] = ""
        if scont_dict["MaxTime"] == "UNLIMITED":
            if scont_dict["MaxWall"] != "":
                english_limits.append(["Max job time limit", scont_dict["MaxWall"]])
        else:
            english_limits.append(["Max job time limit", scont_dict["MaxTime"]])
        for tres in limit_names:
            if scont_dict[tres] != "":
                english_limits += tres_to_english(tres, scont_dict[tres])
        limits[partition] = english_limits
    return defaults, limits


def iprint(i, toprint):
    indent = "    " * i
    print(indent + toprint)


def print_part_table(i, partition, hardware_list, has_gpus, defaults, limits):
    if has_gpus:
        cols = out_cols_gpu
    else:
        cols = out_cols

    iprint(0 + i, f'=== "{partition.rstrip("*")}"\n')
    if partition in commons:
        iprint(1 + i, commons[partition] + "\n")
    iprint(1 + i, "**Request Defaults**\n")
    iprint(
        1 + i,
        f"Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.\n",
    )
    iprint(1 + i, "``` text")
    iprint(1 + i, defaults)
    iprint(1 + i, "```\n")
    if has_gpus:
        iprint(1 + i, '!!! warning "GPU jobs need GPUs!"')
        iprint(
            2 + i,
            "Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.",
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
    for line in part_hardware[partition]:
        iprint(1 + i, "|" + "|".join([line[col] for col in cols]) + "|")
    print("")


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
pi_parts = [part for part in part_hardware if part.startswith("pi_")]
if len(pi_parts) > 0:
    print("### Private Partitions")
    print(
        "With few exceptions, jobs submitted to `pi_` partitions are not considered when calculating your group's [Fairshare](/clusters-at-yale/job-scheduling/fairshare/). Your group can purchase additional hardware for private use, which we will make available as a `pi_groupname` partition. These nodes are purchased by you, but supported and administered by us. After vendor support expires, we retire compute nodes. Compute nodes can range from $10K to upwards of $50K depending on your requirements. If you are interested in purchasing nodes for your group, please [contact us](/#get-help).\n"
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
