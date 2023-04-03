# tmux

`tmux` is a "terminal multiplexer", it enables a number of terminals (or windows) to be accessed and controlled from a single terminal. `tmux` is a great way to save an interactive session between connections you make to the clusters. You can reconnect to the session from a workstation in your lab or from your laptop from home!

## Get Started

To begin a `tmux` session named myproject, type

``` bash
tmux new -s myproject
```

You should see a bar across the bottom of your terminal window now that gives you some information about your session. If you are disconnected or detached from this session, anything you were doing will still be there waiting when you reattach

The most important shortcut to remember is <kbd>Ctrl</kbd>+<kbd>b</kbd> (hold the ctrl or control key, then type "b"). This is how you signal to `tmux` that the following keystroke is meant for it and not the session you are working in. For example: if you want to gracefully detach from your session, you can type <kbd>Ctrl</kbd>+<kbd>b</kbd>, then <kbd>d</kbd> for detach. To reattach to our sample `tmux` session after detatching, type:

``` bash
tmux attach -t myproject
#If you are lazy and have only one session running,
#This works too:
tmux a
```

Lines starting with a "#" denote a commented line, which aren't read as code

Finally, to exit, you can type `exit` or <kbd>Ctrl</kbd>+<kbd>d</kbd>

## tmux on the Clusters

Using tmux on the cluster allows you to create interactive allocations that you can detach from. Normally, if you get an interactive allocation (e.g. `salloc`) then disconnect from the cluster, for example by putting your laptop to sleep, your allocation will be terminated and your job killed. Using tmux, you can detach gracefully and tmux will maintain your allocation. Here is how to do this correctly:

1. ssh to your cluster of choice
1. Start tmux
1. Inside your tmux session, submit an interactive job with `salloc`. See the [Slurm documentation](/clusters-at-yale/job-scheduling#interactive-jobs) for more details
1. Inside your job allocation (on a compute node), start your application (e.g. matlab)
1. Detach from tmux by typing <kbd>Ctrl</kbd>+<kbd>b</kbd> then <kbd>d</kbd>
1. Later, on the _same_ login node, reattach by running `tmux attach`

Make sure to:

* run tmux on the login node, NOT on compute nodes
* run `salloc` inside tmux, not the reverse.

!!!warning
    Every cluster has two login nodes.  If you cannot find your tmux session, it might be running on the other node.  Check the hostname of your current login node (from either your command prompt or from running `hostname -s`), then use ssh to login to the other one.  
    For example, if you are logged in to grace1, use `ssh -Y grace2` to reach the other login node.


### Windows and Panes

`tmux` allows you to create, toggle between and manipulate panes and windows in your session. A window is the whole screen that `tmux` displays to you. Panes are subdivisions in the curent window, where each runs an independent terminal. Especially at first, you probably won't need more than one pane at a time. Multiple windows can be created and run off-screen. Here is an example where this may be useful.

Say you just submitted an interactive job that is running on a compute node inside your `tmux` session.

``` bash
[ms725@grace1 ~]$ tmux new -s analysis
# I am in my tmux session now
[ms725@grace1 ~]$ salloc
[ms725@c14n02 ~]$ ./my_fancy_analysis.sh
```

Now you can easily monitor its CPU and memory utilization without ever taking your eyes off of it by creating a new pane and running `top` there. Split your window by typing:

<kbd>Ctrl</kbd>+<kbd>b</kbd> then <kbd>%</kbd>

`ssh` into the compute node you are working on, then run top to watch your work as it runs all from the same window.

``` bash
# I'm in a new pane now.
[ms725@grace1 ~]$ ssh c14n02
[ms725@c14n02 ~]$ top
```

Your view will look something like this:

![tmux](/img/tmux-michael.png)

To switch back and forth between panes, type <kbd>Ctrl</kbd>+<kbd>b</kbd> then <kbd>o</kbd>
