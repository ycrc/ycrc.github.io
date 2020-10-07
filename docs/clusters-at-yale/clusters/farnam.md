# Farnam

![Louise](/img/Louise-Whitman-Farnam.jpg){: .cluster-portrait}

Farnam is a shared-use resource for the [Yale School of Medicine](https://medicine.yale.edu) (YSM). It consists of a variety of compute nodes networked over ethernet and mounts several shared filesystems.

The Farnam Cluster is named for [Louise Whitman Farnam](http://archives.yalealumnimagazine.com/issues/2006_09/old_yale.html), the first woman to graduate from the Yale School of Medicine, class of 1916.


- - -

## Partitions and Hardware

Farnam is made up of several kinds of compute nodes. We group them into  (sometimes overlapping)  [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. By combining the `--partition` and [`--constraint`](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) Slurm options you can more finely control what nodes your jobs can run on.

### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/farnam_partitions.md"

## Public Datasets

We host datasets of general interest in a loosely organized directory tree in `/gpfs/ysm/datasets`:

```
├── cryoem
├── db
│   ├── annovar
│   ├── blast
│   ├── busco
│   └── Pfam
└── genomes
    ├── 1000Genomes
    ├── 10xgenomics
    ├── Aedes_aegypti
    ├── Chelonoidis_nigra
    ├── Danio_rerio
    ├── Drosophila_melanogaster
    ├── hisat2
    ├── Homo_sapiens
    ├── Mus_musculus
    ├── PhiX
    └── Saccharomyces_cerevisiae
```

If you would like us to host a dataset or questions about what is currently available, please [contact us](/#get-help).

## Storage

Farnam has access to a number of GPFS filesystems. `/gpfs/ysm` is Farnam's primary filesystem where Home, Project, and Scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/index) documentation.

You can check your current storage usage & limits by running the `getquota` command. Your `~/project` and `~/scratch60` directories are shortcuts. Get a list of the absolute paths to your directories with the `mydirectories` command. If you want to share data in your Project or Scratch directory, see the [permissions](/clusters-at-yale/data/permissions/) page.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory       | Storage                                 | File Count | Backups |
|-----------|----------------------|-----------------------------------------|------------|---------|
| home      | `/gpfs/ysm/home`     | 125GiB/user                             | 500,000    | Yes     |
| project   | `/gpfs/ysm/project`  | 1TiB/group, increase to 4TiB on request | 5,000,000  | No      |
| scratch60 | `/gpfs/ysm/scratch60`| 20TiB/group                             | 15,000,000 | No      |

