# Maya

[Autodesk Maya](https://www.autodesk.com/products/maya/) 2026.2 is available on Bouchet as an Apptainer-based module. It includes Arnold, Bifrost, LookdevX, MayaUSD, and Adobe Substance 3D, and is licensed against the YCRC network license server.

## Load the Module

```
module load Maya
```

This puts the following commands on your `PATH`:

| Command        | Purpose                                                  |
| -------------- | -------------------------------------------------------- |
| `mayagui`      | Launch the Maya GUI (interactive, GPU node)              |
| `maya`         | Standard `maya` binary (container-wrapped, headless)     |
| `mayapy`       | Maya's bundled Python interpreter                        |
| `Render`       | Standalone renderer (Arnold, etc.)                       |
| `maya-batch`   | Run a scene in batch mode through a Slurm job            |
| `maya-parallel`| Split a scene's frame range across parallel Slurm jobs   |

## Interactive GUI

The Maya GUI is resource-intensive and requires a GPU to run. We recommend launching it inside a [Remote Desktop session](/clusters-at-yale/access/ood/) on the [Open OnDemand](/clusters-at-yale/access/ood) web portal.

1. From the OOD dashboard, start a **Remote Desktop** session on a GPU partition (e.g. `gpu` or `gpu_devel`), requesting at least 1 GPU, 2 CPUs, and 8GB of memory.
2. Once the desktop opens, launch a terminal and run:

    ```
    module load Maya
    mayagui
    ```

`mayagui` auto-detects the GPU and runs Maya's Viewport 2.0 through VirtualGL. On the first launch it will register your account against the network license server; subsequent launches reuse the cached registration in `~/.autodesk_maya/`.

!!!tip
    If you see "No GPU — VP2 will use software rendering" at startup, you launched on a non-GPU node. Exit and restart on a GPU partition — software rendering is too slow to be usable.

## Batch Mode

For headless runs (rendering, simulation playback, scripted scene processing) use `maya-batch` from inside a Slurm job. An example script is below:

```
#!/bin/bash
#SBATCH --job-name=maya_batch
#SBATCH --partition=day
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G

module load Maya
maya-batch /path/to/your_scene.mb
```

Submit with:

```
sbatch example_batch.sbatch
```

`maya-batch` steps the scene through its full frame range and writes a per-frame CSV of keyframed animation values next to the scene file. Use `maya-batch --help` for the full option list (custom frame range, output directory, etc.).

For arbitrary scripted work, you can also call the underlying `maya` or `mayapy` binaries directly:

```
maya -batch -file scene.mb -command "python(\"import my_module; my_module.run()\")"
mayapy my_script.py
```

## Parallel Mode

For long scenes where each frame is **independent** (pose sweeps, geometry queries driven by pre-keyed animation, etc.), `maya-parallel` splits the frame range across multiple Slurm jobs and merges the resulting CSVs once all chunks finish:

```
module load Maya
maya-parallel scene.mb --chunks 16 --cpus 16 --memory 32G --time 24:00:00
```

This submits 16 chunk jobs plus a dependent merge job that produces `<scene>_results.csv`. Common options:

| Option           | Default                | Description                              |
| ---------------- | ---------------------- | ---------------------------------------- |
| `--chunks N`     | 16                     | Number of parallel chunk jobs            |
| `--cpus N`       | 16                     | CPUs per chunk                           |
| `--memory SIZE`  | 32G                    | Memory per chunk                         |
| `--time DUR`     | 24:00:00               | Wall time per chunk                      |
| `--partition P`  | day                    | Slurm partition for chunk + merge jobs   |
| `--start N`      | auto-detect from scene | First frame                              |
| `--end N`        | auto-detect from scene | Last frame                               |
| `--output-dir D` | `./<scene>_parallel`   | Where chunk CSVs, logs, and results land |

`maya-parallel` is only correct when frames don't depend on prior simulation state — don't use it for cached fluid/cloth sims that carry state forward in time.

## Getting Help

If Maya fails to check out a license, GUI rendering looks corrupt, or a batch job hangs, please [contact us](/#get-help). This is a new and complex software to run on the cluster, so please don't hesitate to reach out for assistance.
