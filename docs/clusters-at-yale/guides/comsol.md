# COMSOL

YCRC has COMSOL Multiphysics 5.2a available on Grace and Farnam. It can be used to run basic physical and multiphysics models on one node utilizing multiple cores. If you need to run run models across multiple nodes or need to run COMSOL on your local machine, please [contact us](/#get-help).

## Use COMSOL

To use COMSOL on the cluster, load the COMSOL module by running `module load COMSOL/5.2a-classkit`. For more information on our modules, please see our [software modules](/clusters-at-yale/applications/modules) documentation. 

COMSOL has a resource intenstive GUI and, therefore, we strongly recommend using COMSOL in a Remote Desktop session on the [Open OnDemand web portal](/clusters-at-yale/access/ood/).

To launch COMSOL in your Remote Desktop, open the terminal application in the session and enter the following commands:

```
module load COMSOL/5.2a-classkit
comsol -np $SLURM_CPUS_ON_NODE &
```

## Run COMSOL in Batch Mode

Comsol can be run without the graphical interface assuming you have a model file and a study defined beforehand. 
This is particularly useful for parametric sweeps or scanning over a range of values for specific parameters.
For example:

```
comsol batch -configuration /tmp -data /tmp -prefsdir /tmp -inputfile mymodel.mph -outputfile out.mph -study std1 
```

which will run the study `std1` found within the `mymodel.mph` file generated through the COMSOL GUI and save the outputs in  `out.mph`. 
A parameter can be passed into the study like this:

```
comsol batch -inputfile  mymodel.mph -outputfile out.mph -pname L -plist 8[cm],10[cm],12[cm]
```
Which will run three versions of the model sequentially for each of the three values of `L` enumerated.
When combined with [Slurm Job Arrays](/clusters-at-yale/job-scheduling/dsq/) many COMSOL jobs can be run in parallel.
An example `dSQ` job-file would look like:

```sh
module load COMSOL; comsol batch -inputfile  mymodel.mph -outputfile out_8.mph -pname L -plist 8[cm]
module load COMSOL; comsol batch -inputfile  mymodel.mph -outputfile out_10.mph -pname L -plist 10[cm]
module load COMSOL; comsol batch -inputfile  mymodel.mph -outputfile out_12.mph -pname L -plist 12[cm]

```
Which would run three versions of the study using different values of `L` and save their outputs in separate files.
Be careful to provide a different output file for each line to avoid clashes between the separate jobs.

More details can be found on the [COMSOL documentation site](https://www.comsol.com/support/knowledgebase/1250).


## Details of COMSOL on YCRC Clusters

Two COMSOL modules (Heat Transfer and Structural Mechanics) are included in addition to the main multiphysics engine.

The following models might be solved using our COMSOL package both in stationary and time dependent studies.

1. *AC/DC.* _Electric Currents and Electrostatics_ in 1D, 2D, 3D models. _Magnetic Fields_ in 2D.

1. *Acoustics.* _Pressure acoustics in frequency domain_ in 1D, 2D, 3D models.

1. *Chemical Species Transport.* _Transport of Diluted Species_ in 1D, 2D, 3D models. Transport and reactions of the species dissolved in a gas, liquid, or solid can be handled with this interface. The driving forces for transport can be diffusion, convection when coupled to a flow field, and migration, when coupled to an electric field. _Moisture Transport_ in 1D, 2D, 3D is used to model moisture transfer in a porous medium.

1. *Fluid Flow.* _Single Phase Laminar and Turbulent Flow_ including non-isothermal flow in 2D, 3D models. _Fluid-Structure Interaction_ in 2D, 3D models for both fixed geometry and deformed solid.

1. *Heat Transfer* in 1D, 2D, 3D models. _HT in Solids and Fluids. HT in porous media including non-equilibrium_ transfer. _Bioheat_ transfer. _Surface to Surface Radiation. Joule Heating. HT in thin structures_ (2D, 3D) like shells, films, fractures. _Conjugate HT_ from laminar and turbulent flows (2D, 3D). _Heat and moisture_ transport. _Thermoelastic_ effect.

1. *Plasma* in 1D. _Equilibrium DC Discharges_ that are sustained by a static or slow-varying electric field where induction currents and fluid flow effects are negligible.

1. *Structural Mechanics* in 2D, 3D models. _Solid Mechanics (elastic). Plate Truss_ in 2D. _Beam, Truss_ (2D, 3D). _Membrane_ (2D axisymmetric, 3D). _Shell_ (3D). _Thermal stress. Thermal expansion. Piezoelectricity._

1. *General Mathematics equations* in 1D, 2D, 3D models. _Classic PDE. Coefficient based and general form PDE. Wave form PDE. Weak form PDE. Ordinary differential equations and algebraic equations. Deformed geometry and moving mesh. Curvilinear coordinates._ 

All above models can be used in the Multiphysics approach of coupling them together. They can be solved in Full Couple mode or by using Segregated Solver (solving one physical model and using resulting field to model another, and so on).


## Backward Compatibility

COMSOL is not backwards compatible. If you have a project file from a newer version of COMSOL (e.g. 5.3), it will not open in 5.2a. However, in some circumstances, we can assist with porting the project file back to version 5.2a. If you have any questions about this, please [contact us](/#get-help).

## Limitations of Available License

Please note that some commonly used COMSOL features such as CAD Import Module, Material Library, and MatLab Link are not included in the license. 

COMSOL Material Library consists of about 2500 different materials with their physical properties. Many of them are included with temperature dependancies. Without this library you have to specify material parameters manually, however, you can save your new material for future use.  We can help in adding material form COMSOL library to your project file using a different license.

You cannot import geometry designed by external CAD program like SolidWorks, Autocad, etc. Instead you have to design it inside COMSOL. However, we can help you to perform such import utilizing different license; we’ll save it in COMSOL project file and you would be able to open it with already imported geometry.

More advanced users often use MatLab for automation of COMSOL models and extracting results data for mining them by external methods available in MatLab. Unfortunately, you cannot do this with the license available on the cluster. Please [contact us](/#get-help) if you feel you need to utilize MatLab.

Lastly, our license does not allow to use COMSOL for solving models based on Maxwell Equations (RF, Wave Optics), semiconductor models, particle tracing, ray optics, non-linear mechanics, and some other more advanced modules. To approach such models in COMSOL on your local computer, please [contact us](/#get-help) to use our more general license with very limited number of licensed seats.
