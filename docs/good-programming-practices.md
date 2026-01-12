# Good Programming Practices :computer:
## Tips & Tricks to Write Code That Makes Sense 

In academic settings, people tend to write code with function in mind: they have a scientific goal to achieve and the time spent coding must lead to that goal only. This strategy can be rewarding once results start coming in, but rewards can be even larger by considering _structure_ and _style_. Code written with no attention to structure or style can be slow to run and difficult to read, with negative effects on its efficiency and reusability. This means that a preprocessing pipeline can run in days instead of hours, or that code written today will not be understood tomorrow &mdash; by colleagues, students, readers of our papers, or our future selves. While code efficiency is a technical topic that requires knowledge and practice, readability and understandability are relatively easy to achieve &mdash; but impactful nonetheless. 

Code is not merely any tool: it is the implementation of a data analysis process. Therefore, the inability to read previously written code is the inability to understand and re-run previous data analyses, which is detrimental to the [reproducibility](https://forrt.org/glossary/english/reproducibility/) of scientific results. The same applies to code that implements behavioural experiments, data transfer between different hardware, and anything else that might occur in a neuroscientific setting. 

Actions resulting in readable and reusable code that yields reproducible results are known as _good programming practices_ (GPPs). GPPs vary between languages and communities: Matlab GPPs can be different from Python GPPs, and neuroscience coders might follow different conventions than engineering coders. However, some practices that impact readability and usability are equally valid across languages and domains. Those practices are _scripting_, _modularity_, _parametrization_, _documentation_, and _using environments or containers_. 

## Table of Contents
1. [Scripting](#1-scripting)
2. [Modularity](#2-modularity)
3. [Parametrization](#3-parametrization)
4. [Documentation](#4-documentation)
5. [Using Environments or Containers](#5-using-environments-or-containers)

## 1. Scripting 
This hands-on activity was based entirely on Jupyter Notebooks, which are great when you need to present code, text and multimedia in a single document. This usually happens in contexts like teaching or step-by-step demonstrations, which require some form of interactive use: the user sits in front of the computer, is interested in attending operations as they happen, and is continuously required to provide inputs (for example, running a notebook cell-by-cell). This is not the case for many real-world scenarios, like the preprocessing of data from an entire neuroimaging experiment. In those cases, users might prefer scripts.

Scripts are simple text files that contain code, with no other addition &mdash; that is, no well-formatted text explanations nor rich media. Python scripts have a `.py` extension and can be read or modified with a variety of tools: advanced code editors like [VSCode](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/) or [Spyder](https://www.spyder-ide.org/), but also simple notepads or the terminal. This repository contains a folder called [`scripts`](/scripts), where you can find `.py` files that reproduce the operations carried out by [`pipeline.ipynb`](/pipeline.ipynb).

Compared to notebooks, scripts are more lightweight, they do not depend on continuous user input, and they lend themselves to [modularity](#2-modularity).

## 2. Modularity
Often, we write our code in a single file that carries out all the operations that we need. In the case of TMS-EEG preprocessing, that would be a single script that does everything from reading the data to calculating statistics on the TEP. The file `scripts/bad_example.py` is one such example, and a bad one: while it can lead to scientifically valid results, the single-script approach has negative effects on the readability, reusability, and adaptability of the code. The reason is that understanding the operations implemented by some code becomes increasingly difficult as the code's length increases, as does locating the parts that might need improvements or corrections. This is especially true in case of complex scripts, where code of actual scientific value (for example, a signal filter) is mixed with (and often, hidden behind) code that implements simple housekeeping tasks, like reading and writing data, changing filenames, reshaping arrays, and similarly mundane (albeit important) things. 

The alternative to giant scripts is _modularity_: a strategy that consists of breaking code into independent sections that can live in different files and be reused in different contexts. For example, so-called _toolboxes_ like [MNE-Python](https://mne.tools/stable/index.html) are collections of code units that carry out single tasks, live in separate files and can be reused indefinitely. When users call MNE-Python functions, they are actually reusing previously written code that was designed with modularity in mind. 

In the context of a TMS-EEG pipeline, modularity can be implemented by distributing the code over three different files: one with reusable [functions](https://realpython.com/defining-your-own-python-function/) (or _utilities_) that implement single preprocessing steps ([`scripts/utils.py`](/scripts/utils.py)), one with modifiable parameters that regulate the behaviour of such functions ([`scripts/config.py`](/scripts/config.py)), and one (the _master script_) that calls all functions in the right order, feeding them the right parameters ([`scripts/pipeline.py`](/scripts/pipeline.py)). With this approach,readers should be able to: 

- Get a sense of the whole pipeline by reading the master script (`pipeline.py`)
- Inspect the specifics of a single step in the utilities file (`utils.py`)
- Easily find and modify a parameter in the configuration file (`config.py`)

The idea of a single file that stores all configurable parameters introduces the concept of _parametrization_.

## 3. Parametrization
Parametrization is the practice of defining free-to-vary parameters instead of hard-coding quantities into a section of code. 

Imagine you have the following list. The numbers in it could mean anything &mdash; for example, they could be timepoints of interest for EEG data analysis:

```python
timepoints = [0,1,2,3,4,5,6,7,8,9]
```

Imagine you want to extract the elements in fourth, fifth, and sixth position &mdash; that is, the items located at indices 3, 4 and 5, because Python counts from 0.
The following code does the job:

```python
timepoints_of_interest = timepoints[3:5]
```

Now imagine two different scenarios:

- In one scenario you are coding a long and complex data analysis pipeline, where the extraction described above is repeated a number of times along the pipeline. The timepoints in fourth, fifth and sixth position represent the times when the subject is seeing stimulus A, but there are other times of potential interest when the subject looks at stimulus B. After discussing with your colleagues, you decide to shift your focus from analysing the response to stimulus A to analysing the response to stimulus B, which occurs later. Because the extraction recurs along the pipeline, you need to change all occurrences of the code above, at risk of forgetting some occurrences and getting odd results in return
- In another scenario you want to reproduce the analyses carried out by the authors of a paper or by a former member of your research  group. You go through their code, find the lines that extract the timepoints of interest and have no idea what numbers like 3 and 5 represent from a scientific point of view: is it the response to stimulus A, the response to stimulus B, or is it something else entirely? 

Both scenarios are extremely common in everyday scientific work. As trivial as they may seem, they can cause very long delays &mdash; especially to beginners, who have no experience to help them understand the cause of errors or find meaning in the code. However, both scenarios can be easily avoided by parametrizing the objects of interest &mdash; that is, assigning them to variables with an informative name, which are defined just once and can be changed forever with a single edit, without having to scroll in search of all occurrences: 

```python
STIMULUS_ONSET, STIMULUS_OFFSET = 3, 5									# changing this

timepoints_of_interest = timepoints[STIMULUS_ONSET:STIMULUS_OFFSET]     # changes that
```

Parameters can be anything from simple indices (as in the example) to the cut frequency of a filter or a statistical significance threshold: they are any quantity that is free to vary and is instrumental to one or more data analysis steps. Ideally, all parameters should be defined in a dedicated file like [`/scripts/config.py`](/scripts/config.py). This should ensure clarity and ease of retrieval, for ourselves as well as future users.  

## 4. Documentation
Reading code written by others is a frequent task for anyone in a research setting, where you can find yourself reading code from colleagues or from the developers of some toolbox. In both cases, the task can be difficult and time-consuming &mdash; especially if the code is not well-documented.

Documentation is text that explains what code does. Roughly speaking, there exists two levels of documentation, which we might call _in-code documentation_ and _out-of-code documentation_.

### 4.1. In-Code Documentation
In-code documentation is a set of conventions that make code understandable without resorting to any external resource. In-code documentation consists of variable names and docstrings. For example, the following Python function has in-code documentation because all names are self-explanatory and there is a docstring (that is, the text in quotes) to explain how the function works:

```python
def add_and_multiply(number1, number2, coefficient):
	"""This function adds two numbers and multiplies them for a coefficient.
	
	Parameters:
	number1 -- the first number to add (type: float)
	number2 -- the second number to add (type: float)
	coefficient -- the coefficient (type: float)
	
	Returns:
	result -- the result of the operation (type: float)
	"""
	
	result = (number1 + number2) * coefficient
	return result
```

Compare this to the following function, which does the same job but without a docstring nor clear variable names:

```python
def addmult(m,n,c):
	y = (m+n)*c
	return y
```

Less clear, right? And even less so if the function serves more complex tasks, like interpolating a TMS pulse in continuous data. The following function is a non-documented example:

```python
from scipy.interpolate import CubicSpline

def tms_interp(eeg, events, pre, post):
	eeg = eeg.copy().get_data().astype("float32")
	chans = eeg.shape[0]
	times = np.arange(eeg.shape[1])
	pre = pre*5000
	post = post*5000

	for n, ev in enumerate(events):
		t = int(event[0])
		interpMin = t - pre
		interpMax = t + post
		mask = np.ones(eeg.shape[1], bool)
		mask[interpMin:interpMax] = False
		idx = t[mask]
		for ch in range(chans):
			data = eeg[channel, mask]
			cs = CubicSpline(idx, data)
			new_indices = np.arange(interpMin,interpMax)
			interp = cs(new_indices)
			eeg[channel, interpMin:interpMax] = interp 

	eeg_interp = mne.io.RawArray(eeg,eeg_data.info)
	return eeg_interp
```

while this is the same function with in-code documentation:

```python
from scipy.interpolate import CubicSpline

def interpolate_pulse_cubic_spline(eeg_data, events_array, interpolate_from, interpolate_to):
	"""Interpolates TMS pulse artifacts with a cubic spline, channel-by-channel. 

	Parameters:
	eeg_data -- continuous EEG data with artifacts to interpolate (type: mne.Raw object)
	events_array -- an array of events. Event times are in column 0 (type: NumPy array)
	interpolate_from -- the start time of the interpolation window, in seconds (type: float)
	interpolate_to -- the end time of the interpolation window, in seconds (type: float)

	Returns:
	post_interpolation_eeg_data -- continuous EEG data with no more artefacts (type: mne.Raw object)
	"""
	
	raw_eeg_time_series = eeg_data.copy().get_data().astype("float32")
	number_of_channels = raw_eeg_time_series.shape[0]
	all_time_points = np.arange(raw_eeg_time_series.shape[1])
	pre_pulse_points = interpolate_from*eeg_data.info["sfreq"]
    post_pulse_points = interpolate_to*eeg_data.info["sfreq"]

	for event_number, event in enumerate(events_array):
		print(f"Processing event {event_number}...")
		event_time = int(event[0])
		artifact_window_min = event_time - pre_pulse_points
		artifact_window_max = event_time + post_pulse_points
		artifact_mask = np.ones(shape=raw_eeg_time_series.shape[1], 
								dtype=bool)
		artifact_mask[artifact_window_min:artifact_window_max] = False
		relevant_time_points = all_time_points[artifact_mask]
		for channel in range(number_of_channels):
			print(f"Working on channel {channel}...")
			data_of_interest = raw_eeg_time_series[channel, artifact_mask]
			cubic_spline = CubicSpline(x=relevant_time_points,
									   y=data_of_interest)
			new_indices = np.arange(start=artifact_window_min,
									stop=artifact_window_max)
			interpolated_pulse = cubic_spline(new_indices)
			raw_eeg_time_series[channel, artifact_window_min:artifact_window_max] = interpolated_pulse 

	post_interpolation_eeg_data = mne.io.RawArray(data=raw_eeg_time_series,
												  info=eeg_data.info)
	return post_interpolation_eeg_data
```
### 4.2. Out-of-Code Documentation
Out-of-code documentation is any information that is useful to understand and use some code, but does not fit inside the code itself. This can be a text guide for how to use the code (typically, a file called README like [this one](https://github.com/matteo-d-m/python-course-cimec-2023/blob/main/README.md)), a website with long-form explanations about a toolbox (for example, [this one](https://mne.tools/stable/index.html)), or a set of instructions on how to make the necessary installations (for example, what you got [here](https://github.com/coneco-lab/brainstim-multimodal?tab=readme-ov-file#installation-instructions)). This last step is particularly important, as any software depends on a set of other software to function correctly, and users who have no information about it are bound to waste their time.

### 4.3. Documentation Checklist
In practice, one can see documentation as the process of going through the following checklist:

- Use informative variable names
- Write docstrings for your functions
- Use READMEs for project repositories
- Give detailed information on dependencies and installation instructions 

# 5. Using Environments or Containers
The following cases occur frequently in settings where people write and share their code, including research groups where multiple people use the same analysis pipeline:

- **Case 1.** You receive code from a colleague. This code relies on a set of _dependencies_ &mdash; that is, software tools that the code is built upon. You try running the code, but you fail because you do not have the dependencies. After a long search that involves a lot of trial-and-error, you figure out the dependencies and install them, but find out that they have further dependencies which you cannot easily retrieve
- **Case 2.** You receive code from a colleague. This code relies on a certain version of a given library, but you have another version. This causes errors in the code or yields suboptimal results because the two library versions differ   
- **Case 3.** You receive code from a colleague. Everything works smoothly, but you get unxpected results due to performance differences between your computing set-up and your colleague's

All three cases are undesirable and can be avoided using environments or containers. 

## 5.1. Anaconda environments
Taking part in the hands-on activity required you to install and use Anaconda. Anaconda is a package and environment manager &mdash; that is, software that orchestrates the interactions between other softwares, allowing users to run multiple computational projects on the same machine without creating conflicts between them. 

When you install Anaconda, you get:

- The Python programming language
- Easy and automated access to a huge variety of Python-based software
- A tool to easily create, manage, and share _environments_

The latter is perhaps Anaconda's most interesting feature. Environments are _"self-contained, isolated spaces where you can install specific versions of software, including dependencies, libraries, and Python versions. This isolation helps avoid conflicts between package versions and ensures that your projects have the exact libraries and tools they need"_ (source: Anaconda documentation &mdash; accessed December 2025). In other words, Anaconda allows researchers to partition their computer into isolated virtual compartments, making sure that each project has all the necessary software and avoiding any conflicts. 

Importantly, the instructions to create environments can be easily saved and shared as text files that are commonly referred to as _environment files_. This was the role of [`brainstim-multimodal.yml`](../brainstim-multimodal.yml): specify all the software that we needed for the hands-on activity in all the appropriate version, so that you could recreate the exact same computing environment that I use with the one-line command `conda env create -f brainstim-multimodal.yml`.

The [Anaconda documentation](https://www.anaconda.com/docs/main) contains detailed concept guides and step-by-step tutorials. You can go through them to start understanding Anaconda: you will soon find out that acquiring a working knowledge is easier and faster than one might think.  

## 5.2. venv & pip
An alternative to Anaconda is [`venv`](https://docs.python.org/3/library/venv.html), which ships directly with a [basic Python installation](https://www.python.org/downloads/). Using `venv` you can create an environment, and using the [`pip`](https://pip.pypa.io/en/stable/) package manager you can install Python packages inside it. As with Anaconda, the resulting software environments can be saved and shared through text files &mdash; which, for the `venv`-`pip` combination, are usually titled `requirements.txt` and can be installed as `pip install -r requirements.txt`.

At a superficial exam, the `venv`-`pip` combination looks the same as Anaconda. However, the two products have several important differences that are well described by [this](https://www.anaconda.com/blog/understanding-conda-and-pip) document on the Anaconda website. In summary, Anaconda has three features that make it more versatile: 

- It is both an environment and a package manager, so you get two services from a single software. In contrast, `venv` is only an environment manager and `pip` is only a package manager, so you need to install them both if you want full service
- Anaconda is mainly focused on Python, but it also includes the R, Julia, and Scala programming languages and a vast array of R packages. In contrast, `venv` environments are specific to Python projects and `pip` has only access to Python packages that are stored on the [Python Package Index (PyPI)](https://pypi.org/)
- [According to Anaconda developers](https://www.anaconda.com/blog/understanding-conda-and-pip), Anaconda does a better job at ensuring that all installed packages have all their dependencies in order

## 5.3. Containers 
Environments created with Anaconda or `venv` are great to package the most direct dependencies of a software project, but cannot package an entire computing environment. In practice, this means that they can package your code's most immediate dependencies and make it easy to share them, but they cannot isolate your code from the surrounding computer. Therefore, your code can still be exposed to reproducibility failures related to system-wide differences between computers, that an Anaconda or `venv` environment cannot control. In these cases, it helps to use containers. 

In the definition of [Moreau et al. (2023)](https://www.nature.com/articles/s43586-023-00236-9), a container is _"a self-contained and executable package that includes all of the necessary components for running a software application, such as system tools, libraries settings and the application itself, as well as any operating system components that are not provided by the host operating system. This means that containers are completely isolated from one another and the host operating system, and they can run anywhere, regardless of the environment"_. In other words, using a container minimizes the probability of encountering reproducibility failures due to differences between computers that extend beyond your analysis code and its most immediate dependencies, thereby avoiding situations where some code runs smoothly on Windows 10 but not on Windows 11, on Linux but not on MacOS, etc. Minor differences might still persist because containers cannot fully modify the way your code exploits hardware resources, but those differences should be negligible.

# Contacts

For questions or comments, you can contact: 

:question: Matteo De Matola ([UniTN](https://webapps.unitn.it/du/en/Persona/PER0247884/Curriculum), [GitHub](https://github.com/matteo-d-m))

:mailbox: matteo [dot] dematola [at] unitn [dot] it