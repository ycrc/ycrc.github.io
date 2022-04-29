# VirtualGL

## Why VirtualGL

To display a 3D application running remotely on a cluster, you could use X11 forwarding 
to display the application on your local machine. This is usually very slow and often unusable. 

An alternative approach is to use VNC - also called Remote Desktop - to run GUI applications remotely on the cluster. 
This approach only works well with applications that only need moderate 3D rendering where software rendering is good enough.  
For applications that need to render large complicated models, hardware accelerated 3D rendering must be used.  

However, VNC cannot directly utilize the graphic devices on the cluster for rendering. 
[VirtualGL](https://virtualgl.org), in conjunction with VNC, provides a commonly used 
solution for remote 3D rendering with hardware acceleration.


## How to use VirtualGL 

VirtualGL 3.0+ supports the traditional GLX back end and the new EGL back end for 3D rendering. 

The EGL back end uses a DRI (Direct Rendering Infrastructure) deivice to access a graphics device, 
while the GLX back end uses an X server to access a graphics device. 
The EGL back end allows simultaneous jobs on the same node, each using their own dedicated GPU device for rendering.
Although it can render many applications properly, the EGL back end may fail to render some applications.
The GLX back end supports a wider range of OpenGL applications than the EGL back end, however, only one
X server can work properly with the graphics devices on the node. This means only one job can use
the GLX back end on any GPU node, no matter how many GPU devices the node has.

We suggest you use the EGL back end first. If it does not render your application properly, then switch to the GLX back end. 

We have provided a wrapper script `ycrc_vglrun` to make it easy for you to
choose which back end to use for 3D rendering. In the following examples, we will use ParaView
(unless mentioned otherwise) to demonstrate how to use `ycrc_vglrun`.

!!!note
    If you need to run a hardware accelerated GUI application, you should first start
    a Remote Desktop on a GPU node, and then run the application from the shell in the Remote Desktop as shown below.
    We have not incorporated VirtualGL into the standalone interactive Apps on OOD that could benefit from VirtualGL.
    However, this could change in the future.

### Use VirtualGL with the EGL back end

EGL is the default back end which `ycrc_vglrun` will choose to use if no option is provided. You can also add the `-e` 
option to choose the EGL back end explicitly. 

```bash
module load ParaView
ycrc_vglrun paraview
```

```bash
module load ParaView
ycrc_vglrun -e paraview
```

### Use VirtualGL with the GLX back end

If your application cannot be rendered properly with the EGL back end, your next step is to try the GLX back end. 
You should choose it explicitly with the `-g` option. 

```bash
module load ParaView
ycrc_vglrun -g paraview
```

### Run MATLAB with hardware OpenGL rendering

By default, MATLAB will use software OpenGL rendering. To run MATLAB with hardware OpenGL rendering, 
add `-nosoftwareopengl`.
```bash
module load MATLAB
ycrc_vglrun matlab -nosoftwareopengl
```

## Troubleshoot

### `nvidia-smi` or `vglrun` cannot be found

You must submit your job to a GPU node. If you are using the Remote Desktop from OOD, 
make sure you have specified `gpu` as `1` and `partition` as `gpu` or any other partition
with GPU nodes.

### GLX back end is used by another application

If you get the following message when running your application with the GLX back end,
you need to add `--exclude=nodename` to `Advanced options` in the Remote Desktop OOD user interface
and resubmit Remote Desktop. Replace `nodename` with the actual node name from the message. 

```bash
    VirtualGL with the GLX back end is currently used by another application.
    Please resubmit your job with
     
              --exclude=c22n01
```




