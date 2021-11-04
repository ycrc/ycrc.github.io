# Batch-mode grapical programs with XVFB

Often there is a need to run a program with a graphical interface in batch mode.
This can be either due to extended run-time or the desire to run many instances of the process at once. 
In either case the lack of a display can prevent the program from running.

A solution has been developed to create a virtual display that only lives in memory.
This allows the program to happily launch its graphical interface while in batch mode.

!!!note
    It is common for R to require a display session to save certain types of figures. 
    You may see a warning like "unable to start device PNG" or "unable to open connection to X11 display".
    `xvfb` can help avoid these issues.

This tool is called the `X Virtual Frame Buffer` or `xvfb`.
It can act as a wrapper to your script which creates a virtual display session.
For example, to run an R script (e.g. `make_jpeg.R`)  which needs a display session in order to save a JPEG file:

```sh
xvfb-run Rscript make_jpeg.R

```

For more details and other examples see the `xvfb-run` man page by running `man xvfb-run` on any compute node.
