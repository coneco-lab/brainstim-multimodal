# Installing Python Through Miniconda 

We will be managing our Python installation using `conda`. `conda` is a package and environment manager &mdash; that is, software that orchestrates the interaction between other software within isolated virtual spaces called _environments_. In simpler words, `conda` allows you to create isolated virtual compartments inside your computer, making sure that each project has all the necessary software and avoiding any conflicts. 

There are two versions of Anaconda: one is called Anaconda Distribution, the other is called Miniconda. We will use Miniconda because it is much lighter than Anaconda Distribution, but it still has all the features we need.

Installing Miniconda will automatically install base Python, while domain-specific Python packages (for example, MNE-Python) will be installed later with a dedicated operation.

### 1. Download and install Miniconda
Go [here](https://www.anaconda.com/download/success?reg=skipped-miniconda) and download the latest **Miniconda** installer for your operating system. 

> [!WARNING]
> Once you click on the link above, you will face two options: `Anaconda Distribution` (on the left) and `Miniconda` on the right.
> **Ignore `Anaconda Distribution`, choose `Miniconda`**

After the download, run the installer and follow the instructions. I recommend installing `conda` in your home directory to make it easy to find and manage. To this end, make sure it is directly under:

- `C:\Users\your-username\` (if Windows)
- `/Users/your-username/` (if Mac)
- `/home/your-username/` (if Linux)

#### Test your `conda` installation
If you are using Windows, open an Anaconda prompt (use the Windows search tool to find it). If you are using Mac or Linux, open a generic Terminal. 

Once opened your Anaconda prompt or Terminal, type `conda`. If you see a list of commands, you are good to go. If you get something like `conda: command not found`, ask Matteo for help.

---
### 2. Install Jupyter in the base environment
We will install Jupyter in the so-called _base_ environment, where it will accessible to any Python environment we create. 

In your terminal/Anaconda prompt, make sure you see `(base)` at the start of your prompt. If you see it, run:

```bash
conda install -c conda-forge jupyterlab
```

This will install Jupyter and all its dependencies in the base environment. If you are asked to confirm the installation, type `y` and press enter.

Once the installation is complete, you can go back to [the previous page](../README.md#installation-instructions) and keep following the instructions.
