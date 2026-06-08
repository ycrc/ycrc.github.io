# Pymol

The [PyMol](https://pymol.org) molecular visualization system was originally created as open source software written in Python by the late [Warren L. DeLano](https://en.wikipedia.org/wiki/Warren_Lyford_DeLano) (Yale class of 1993). Schrödinger, LLC acquired the project and now compiles and sells [ready-to-run binaries](https://www.pymol.org/#download) for Windows, Mac, and Linux. PyMOL is a trademark of Schrödinger, LLC.


## Open-Source Installation

As an alternative to buying a license, the open-source version of Pymol is available via [conda](https://anaconda.org/channels/schrodinger/packages/pymol/overview). To install on your machine, please use the following instructions. This method works with only minor variations on Windows, Mac and Linux.

1. **Install miniconda** : As of 2026, we recommend using the [Miniforge3 installer](https://conda-forge.org/download/) for miniconda. Alternatively, you may download the [free Miniconda3 version](https://www.anaconda.com/docs/getting-started/miniconda/main#latest-miniconda-installer-links) from the commercial Anaconda website. These two miniconda variants are functionally equivalent (at least for the purposes of Pymol); the trade-off is less burdensome licensing requirements for the Miniforge3 version, vs. better documentation for the commercial version (for example, see [this installation guide](https://www.anaconda.com/docs/getting-started/miniconda/install/windows-gui-install)).

    - Windows: Double-click the installer to run, and click through all the steps to install with default options (please choose the `User` install unless you know what you are doing). Note, you can also customize the installation to taste- this will not interfere with Pymol.

    - Mac/Linux: open a standard terminal window (this is the 'Terminal' app in MacOS) and then type the following command to run the installer.

    !!! Note
        When the installer asks to automatically initialize conda, **respond yes to the 'Proceed with initialization?' prompt. _This is not the default!_ **
    
    ``` sh
    cd ~/Downloads                   # or wherever the downloaded file is
    bash Miniforge3-Darwin-arm64.sh  # substitute as appropriate: Miniforge3-Linux-x86_64.sh, etc.

    # Prevent conda from affecting default Python settings in your terminal windows:
    ~/miniforge3/bin/conda config --set auto_activate_base false
    ```

2. **Start a terminal** : This sets you up to run the Pymol installation command(s) in the next step.

    - MacOS or Linux: Open a standard terminal window ('Terminal' app in MacOS)

    - Windows: Open 'Miniforge Prompt' (type 'miniforge prompt' in the Windows search box). Note that installation can be done in the 'Command Prompt' or 'Powershell', but it takes additional steps (experts only).

3. **Install Pymol** : In the terminal window, run the following:

    - Linux or Windows:
    ```sh
    conda create -n pymol -c conda-forge -c schrodinger pymol-open-source
    ```

    - MacOS ONLY:
    ```sh
    conda create --platform osx-64 -n pymol
    conda activate pymol
    conda install -c conda-forge -c schrodinger pymol-open-source
    ```

    !!! tip
        If you do wish to use the licensed Pymol version, you may also install this with conda (rather than the download links above) by substituting 'pymol-bundle' in place of 'pymol-open-source' in the installation commands above (see also [the Pymol conda docs](https://pymol.org/conda/))


4. **Run Pymol** : The resulting pymol application is found at the following locations:

    - Windows: `C:\Users\<username>\Miniconda3\Scripts\pymol.bat`
    - MacOS:   `/Users/<username>/miniconda3/envs/pymol/bin/pymol`
    - Linux:   `/home/<username>/miniconda3/envs/pymol/bin/pymol`

5. **Create GUI links** : For all three operating systems, app files may be launched in the GUI by double-clicking. For convenience, you may also create an alias to readily launch Pymol with the GUI:

    - Windows or MacOS:
        - Right click->'Create Shortcut'/'Make Alias' (respectively)
        - Move the shortcut to your Desktop or other desired location

    - Linux (terminal): `ln -s <orig-path-to>/pymol /home/<username>/Desktop/pymol`

