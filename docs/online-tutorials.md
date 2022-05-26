# Online Tutorials

## Linux/Unix and Command Line

### Introduction to Linux

* [YCRC Workshop: Practical Introduction to Linux](https://ycrc.github.io/PIL/), ([Video](https://research.computing.yale.edu/ycrc-bootcamp-practical-introduction-linux)) *Recommended
* [Most Commonly Used Commands - RedHat.com](https://www.redhat.com/sysadmin/10-commands-terminal)
* [Command Line for Beginners - Ubuntu.com](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)

Note: You can learn more about most commands you come across by typing "man [command]" into the terminal.

### `awk` (text extraction/parsing)

`awk` is a tool for parsing text and extracting certain section. It is particularly useful for extracting, and even reordering, columns out of tables in text files.

* [Introduction to `awk` and examples of common usage](https://www.freecodecamp.org/news/the-linux-awk-command-linux-and-unix-usage-syntax-examples/)
* [In-depth guide to `awk` and more advanced usage](https://linuxize.com/post/awk-command/#how-awk-works)

### `grep`

Grep is tool for searching command line output or files for a certain string (phrase) or regular expression.

* [Introduction to `awk` and examples of common usage](https://www.freecodecamp.org/news/grep-command-tutorial-how-to-search-for-a-file-in-linux-and-unix/)
* [In-depth guide to `awk` and more advanced usage](https://www.geeksforgeeks.org/grep-command-in-unixlinux/)

### `sed`

`sed` (Stream EDitor) is a tool for making substitutions in a text file. For example, it can be useful for cleaning (e.g. replace NAN with 0) or reformatting data files. The syntax `sed` uses for substitutions is common in Linux (for example, the same syntax is used in the VIM text editor).


* [Introduction to `sed` and examples of common usage](https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/?ref=lbp)
* [In-depth guide to `sed` and more advanced usage](https://www.gnu.org/software/sed/manual/sed.html)

### SSH (connecting to the clusters or other remote linux servers)

* [Connecting to the Yale clusters](/clusters-at-yale/access)
* [Transfer files to/from the cluster](/clusters-at-yale/data/transfer)
* [Advanced SSH configuration](clusters-at-yale/access/advanced-config)
* [In-depth guide to `ssh`](https://www.ssh.com/academy/ssh/command)

### Bashrc and Bash Profiles

* [What is the `.bashrc` and `.bash_profile`?](https://www.linuxfordevices.com/tutorials/linux/bashrc-and-bash-profile)
* [Set aliases for commonly used commands]
* [Environment variables]

### tar or tar.gz archive

`.tar` or `t.ar.gz` are common archive (compressed file) formats. Software and data will frequently be distributed in one of these archive formats.
The most common command for opening and extracting the contents of a `tar` archive is `tar xvf archive.tar` and, for a `tar.gz` archive, `tar xvzf archive.tar.gz` .
See the following link(s) for more details on creating `tar` files and more advanced extraction options.

* [Creating and extracting from a tar file](https://www.howtogeek.com/248780/how-to-compress-and-extract-files-using-the-tar-command-on-linux/)

## Install Windows and Linux on the same computer

### Windows for Linux

It is possible to run Linux terminals and applications from within a Windows installation using the "Windows Subsystem for Linux".

* [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about)

### Dual Boot

"Dual Boot" means you have two separate installations for Windows and Linux, respectively, that switch between by restarting your computer.

* [Dual Boot Linux Mint and Windows](https://itsfoss.com/guide-install-linux-mint-16-dual-boot-windows/)
* [Dual Boot Ubuntu and Windows](https://www.tecmint.com/install-ubuntu-16-04-alongside-with-windows-10-or-8-in-dual-boot/)

## Python

### Intro to Python

* [Fantastic resource for anyone interested in Python](http://www.automatetheboringstuff.com)
* [LinkedIn Learning: Learning Python (Yale only)](https://www.linkedin.com/learning/learning-python-2/python-functions?u=2110361)

### Parallel Programming with Python

* [Quick Tutorial: Python Multiprocessing](https://further-reading.net/2017/01/quick-tutorial-python-multiprocessing/)
* [Parallel Programming with Python](https://chryswoods.com/parallel_python/index.html)
* [YCRC Workshop: Parallel Python](http://docs.ycrc.yale.edu/parallel_python/)

### mpi4py

* [YCRC Workshop: mpi4py](https://research.computing.yale.edu/sites/default/files/files/mpi4py.pdf)
* [mpi4py example scripts](https://github.com/ycrc/mpi4py-examples)
* [Documentation for mpi4py](https://mpi4py.readthedocs.io/en/stable/tutorial.html)

## R

### Intro to R

* [Brief intro to R](http://www.r-tutor.com/r-introduction)
* [Thorough intro to R](https://www.cyclismo.org/tutorial/R/)
* [Another thorough intro to R](https://r-coder.com/learn-r/)

### foreach

* [Using the foreach package - Steve Weston](https://cran.r-project.org/web/packages/foreach/vignettes/foreach.html)

### foreach + dompi

* [Introduction to doMPI](https://cran.r-project.org/web/packages/doMPI/vignettes/doMPI.pdf)

## Matlab

* [Mathworks Online Classses](https://matlabacademy.mathworks.com/)

## Singularity / Apptainer

### Documentation

Singularity has officially been renamed Apptainer, but we expect no changes to its functionality.
 
* [Apptainer Docs Page](https://apptainer.org/docs/user/main/)
* [Singularity Google Groups](https://groups.google.com/a/lbl.gov/forum/#!forum/singularity)

### Tutorials

* [YCRC Workshop: Containers](http://docs.ycrc.yale.edu/containers-bootcamp)
* [NIH tutorial on Singularity](https://singularity-tutorial.github.io)
* [NVIDIA tutorial for using GPUs with Singularity](https://devblogs.nvidia.com/docker-compatibility-singularity-hpc/)
