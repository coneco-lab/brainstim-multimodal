# Installing Python Through Miniconda 

We will be managing our Python installation using `conda`. `conda` is a package and environment manager &mdash; that is, software that orchestrates the interaction between other software within isolated virtual spaces called _environments_. Environments are _"self-contained, isolated spaces where you can install specific versions of software, including dependencies, libraries, and Python versions. This isolation helps avoid conflicts between package versions and ensures that your projects have the exact libraries and tools they need"_ (source: Anaconda documentation &mdash; accessed December 2025). In other words, Anaconda allows you to partition your computer into isolated virtual compartments, making sure that each project has all the necessary software and avoiding any conflicts. 

There exist two versions of Anaconda: one is called Anaconda Distribution, the other is called Miniconda. We will use Miniconda because it has all the features we need and is much lighter than Anaconda Distribution. Installing Miniconda will automatically install base Python, while domain-specific Python packages (for example, MNE-Python) will be installed later with a dedicated operation.

### 1. Download and install (Mini)`conda`
Go [here](https://www.anaconda.com/download/success?reg=skipped-miniconda) and download the latest **Miniconda** installer for your operating system. 

> [!WARNING]
> Once you click on the link above, you will face two options: `Anaconda Distribution` (on the left) and `Miniconda` on the right.
> **Ignore `Anaconda Distribution`, choose `Miniconda`**

After the download, run the installer and follow the instructions. The only option I recommend checking and changing if needed is the installation path. I recommend installing `conda` in your home directory, so that it is easy to find and manage. Make sure it is directly under:

- `C:\Users\your-username\` (if Windows)
- `/Users/your-username/` (if Mac)
- `/home/your-username/` (if Linux)

#### Test your `conda` installation
If you are using Windows, open an Anaconda prompt (you can search it with the Windows search tool). If you are using Mac or Linux, open a generic Terminal. Once opened, type `conda`. If you see a list of commands, you are good to go. If you get something like `conda: command not found`, ask us for help.

---
### 2. Install Jupyter in the base environment
We will install Jupyter in the so-called base environment, where it will accessible to any Python environment we create. 

In your terminal/Anaconda prompt, make sure you see `(base)` at the start of your prompt. If you see it, run:

```bash
conda install -c conda-forge jupyterlab
```

This will install Jupyter and all its dependencies in the base environment. If you are asked to confirm the installation, type `y` and press enter.

#### Test your Jupyter installation
Type the following command in the terminal:

```bash
jupyter lab
```

You should see a browser opening with a Jupyter notebook interface. If you get something like `jupyter: command not found`, you might want to close the terminal and open it again. If the problem persists, ask for help!

---

> [!NOTE]
> The instructions above are modified from Luigi Petrucco's installation guide, which was written for students of CIMeC's PhD course in Cognitive & Brain Sciences 
> (2025 iteration). The original one can be found [here](https://github.com/vigji/python-cimec-2025/blob/main/docs/python-installation.md).
> The link to the original version is provided for citation only: students of Brain Stimulation & Multimodal Electrophysiological Recording should only follow the excerpt given above. 
