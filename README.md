# **Brain Stimulation & Multimodal Electrophysiological Recording &mdash; Hands-on!**

This repository contains Python code for hands-on TMS-EEG preprocessing activities offered as part of the [Brain Stimulation & Multimodal Electrophysiological Recording](https://unitn.coursecatalogue.cineca.it/insegnamenti/2025/50512_653501_96292/2011/50513/10168?annoOrdinamento=2011&coorte=2024) course at the [Master's Degree in Cognitive Science &mdash; Cognitive Neuroscience track](https://corsi.unitn.it/en/cognitive-science/program/overview), University of Trento (academic year 2025/2026). 

The code is structured in a single Jupyter Notebook called `pipeline.ipynb`. A Jupyter Notebook is an interactive document that contains a mix of static text and executable code. The static text can be enriched with mathematical formulas and media such as images or videos, making notebooks a powerful tool to write and present code with explanations.

The goal of the hands-on activities is to progressively populate `pipeline.ipynb` with all the basic steps of a TMS-EEG preprocessing pipeline, complementing the Python code with explanations about what it does, its scientific goal and its effect on the data (for example: _"The following code applies a low-pass filter to the data to attenuate high-frequency signals that are unlikely to be cerebral. As can be seen in the plots, the code achieves its goal... etc."_). 

The hands-on activities will unfold over a series of in-person meetings with the course tutor [Matteo De Matola](https://webapps.unitn.it/du/en/Persona/PER0247884/Curriculum). The meetings will come in pairs made by a _pre_ meeting and a corresponding _post_ meeting, interleaved by a home assignment for the students.

- In the _pre_ meeting, Matteo will introduce a set of preprocessing steps, their scientific goal and their Python implementations. This will help revise the theory introduced in the main lectures and translate it into practice. Students will leave the meeting with working Python code provided by Matteo, but they will be free to write their own implementations should they have Python skills at the appropriate level 
- At home, the students will run the code presented during the _pre_ meeting and comment on its outputs, applying the concepts that they have learned in class. In this phase, students will work on their own copy of `pipeline.ipynb`, writing their comments in the appropriate text cells in an academic style. Students are expected to work independently, but Matteo will be available via email to help them solve technical problems or clarify any doubts. At the end of their work, students will submit their own copy of `pipeline.ipynb`, complete with comments, by 09:00 AM on the day of the _post_ meeting (that is, if the _post_ meeting is on Monday, submit your work by 09:00 AM on Monday)
- In the _post_ meeting, Matteo will provide the students with the correct comments and lead an in-depth discussion of any issues (technical or theoretical) that may arise. After the _post_ meeting, Matteo will update this repository with the latest version of `pipeline.ipynb`, containing his own comments for future reference

Everyone is free to attend the meetings, meaning that attendance does not imply a commitment to carrying out the assignments and respect the deadlines. However, students that want to take the exam under Option A _must_ attend and they _must_ submit all home assignments by the deadline. 

A maximum of one absence to the meetings will be tolerated (though strongly discouraged). Late submissions will not be tolerated in the absence of a documented cause such as debilitating illness or other accidents. 

## **Calendar**

_Pre_ and _post_ meetings will be as follows:

|Topic                               |_Pre_ Meeting |_Post_ Meeting |
|------------------------------------|--------------|---------------|
|Installations check, general Q&A    |Single meeting on Day xx Month|
|------------------------------------|--------------|---------------|
|Basic preprocessing                 |Day xx Month  |Day xx Month   |
|- Reading data                      |              |               |
|- Interpolating the pulse artifact  |              |               |
|- Downsampling                      |              |               |
|- Filtering                         |              |               |
|------------------------------------|--------------|---------------| 
|Independent Component Analysis (ICA)|Day xx Month  |Day xx Month   |
|- Rationale                         |              |               |
|- Fitting                           |              |               |
|- Components selection              |              |               |       
|------------------------------------|--------------|---------------| 
|Manual artifact rejection           |Day xx Month  |Day xx Month   |
|------------------------------------|--------------|---------------|
|Assessing & computing a TEP         |Day xx Month  |Day xx Month   |


## **Installation Instructions**

To participate in the hands-on activities, you will need a laptop with a working Python installation and all the necessary Python-based software like [MNE-Python](https://mne.tools/stable/index.html). To this end, you will need to go through the steps below _before the start of the hands-on activities_:

1. Click on [this](https://github.com/vigji/python-cimec-2025/blob/main/docs/python-installation.md) link and follow the instructions at points 1-2 (that is, until _Create a new Python environment_ included)
2. In a terminal, make sure that your new environment is activated (that is, make sure you have executed `conda activate course-env` without errors). Then, run the following code:

```
cd <insert name of the directory where you want to save this project>
git clone https://github.com/coneco-lab/brainstim-multimodal.git
conda env create -f brainstim-multimodal-env.yml
```
---

Matteo De Matola ([UniTN](https://webapps.unitn.it/du/en/Persona/PER0247884/Curriculum), [GitHub](https://github.com/matteo-d-m))
matteo [dot] dematola [at] unitn [dot] it

