# **Brain Stimulation & Multimodal Electrophysiological Recording &mdash; Hands-on!**

This repository contains Python code for hands-on TMS-EEG preprocessing activities offered as part of the [Brain Stimulation & Multimodal Electrophysiological Recording](https://unitn.coursecatalogue.cineca.it/insegnamenti/2025/50512_653501_96292/2011/50513/10168?annoOrdinamento=2011&coorte=2024) course at the [Master's Degree in Cognitive Science &mdash; Cognitive Neuroscience track](https://corsi.unitn.it/en/cognitive-science/program/overview), University of Trento (academic year 2025/2026). 

## General facts

The code is structured in a single Jupyter Notebook called `pipeline.ipynb`. A Jupyter Notebook is an interactive document that contains a mix of static text and executable code. The static text can be enriched with mathematical formulas and media such as images or videos, making notebooks a powerful tool to write and present code with explanations.

The goal of the hands-on activities is to progressively populate `pipeline.ipynb` with all the basic steps of a TMS-EEG preprocessing pipeline, complementing the Python code with explanations about what it does, its scientific goal and its effect on the data (for example: _"The following code applies a low-pass filter to the data to attenuate high-frequency signals that are unlikely to be cerebral. As can be seen in the plots, the code achieves its goal... etc."_). 

The hands-on activities will unfold over a series of in-person meetings with the course tutor [Matteo De Matola](https://webapps.unitn.it/du/en/Persona/PER0247884/Curriculum). The meetings will come in pairs: a _pre_ meeting and a corresponding _post_ meeting, interleaved by home assignments for the students. The home assignments will count for the final exam if students choose to take the exam under Option A as described below.

- In the _pre_ meeting, Matteo will introduce a set of preprocessing steps, their scientific goal and their Python implementations. This will help revise the theory introduced in the main lectures and translate it into practice. Students will leave the meeting with working Python code provided by Matteo, but they will be free to write their own implementations should they have Python skills at the appropriate level 
- At home, the students will run the code presented during the _pre_ meeting and comment on its outputs, applying the concepts that they have learned in class. In this phase, students will work on their own copy of `pipeline.ipynb`, writing their comments in the appropriate text cells in an academic style. Students are expected to work independently, but Matteo will be available via email to help them solve technical problems or clarify any doubts. At the end of their work, students will submit their own copy of `pipeline.ipynb`, complete with comments, by 09:00 AM on the day of the _post_ meeting (that is, if the _post_ meeting is on Monday, submit your work by 09:00 AM on Monday)
- In the _post_ meeting, Matteo will provide the students with the correct comments and lead an in-depth discussion of any issues (technical or theoretical) that may arise. After the _post_ meeting, Matteo will update this repository with the latest version of `pipeline.ipynb`, containing his own comments for future reference

## The exam in mind

As explained in class, students that attend the Brain Stimulation & Multimodal Electrophysiological Recording course have two options: 

1. **Option A:** write a grant proposal for a study involving brain stimulation and multimodal electrophysiological recording, attend the hands-on preprocessing activity and carry out the related assignments. Assignments for the hands-on activity must be submitted to Matteo as described above (that is, by 09:00 AM on the day of _post_ meetings), while the grant proposal can be submitted to prof. Miniussi (with prof. Belardinelli in cc) at any moment between the end of the course and 1 March 2026. The final grade will be the average of the two grades and will be registered in the 2026 Summer session 
2. **Option B:** take an oral exam about the whole program in any exam session

Everyone is free to attend the meetings, meaning that attendance does not imply a commitment to carrying out the assignments and respect the deadlines. 

However, students that want to take the exam under Option A _must_ attend the _pre-post_ meetings and they _must_ submit all home assignments by the deadline. 

A maximum of one absence to the meetings will be tolerated (though strongly discouraged). Late submissions will not be tolerated in the absence of a documented cause such as debilitating illness or other accidents. 

## **Calendar**

Meetings will be as follows:

0. **Installations check, general Q&As** 
dd/mm/yyyy at Place
1. **Basic preprocessing:** rationale, interpolating the pulse artifact, downsampling, filtering 
    - _Pre_ meeting dd/mm/yyyy at Place, _Post_ meeting dd/mm/yyyy at Place 
2. **Independent component analysis (ICA):** rationale, fitting, components selection  
    - _Pre_ meeting dd/mm/yyyy at Place, _Post_ meeting dd/mm/yyyy at Place
3. **Manual artifact rejection:** rationale and execution 
    - _Pre_ meeting dd/mm/yyyy at Place, _Post_ meeting dd/mm/yyyy at Place
4. **Assessing & computing a TEP** 
    - _Pre_ meeting dd/mm/yyyy at Place, _Post_ meeting dd/mm/yyyy at Place

## **Installation instructions**

To participate in the hands-on activities, you will need a laptop with a working Python installation and all the necessary Python-based software like [MNE-Python](https://mne.tools/stable/index.html). To this end, you will need to go through the steps below _before the start of the hands-on activities_:

1. Click on [this](https://github.com/vigji/python-cimec-2025/blob/main/docs/python-installation.md) link and follow the instructions at points 1-2 (that is, until _Create a new Python environment_ included)
2. In a terminal, make sure that your new environment is activated (that is, make sure you have executed `conda activate course-env` without errors). Then, run the following code:

```
cd <insert name of the directory where you want to save this project>
git clone https://github.com/coneco-lab/brainstim-multimodal.git
conda env create -f brainstim-multimodal-env.yml
```

If you have problems with any of the steps above you are welcome to seek assistance from Matteo. Meeting 0 will be purposedly dedicated to this. To make the meeting smoother, students are warmly invited to try making their installations at home _before_ the meeting.

## Contacts

Matteo De Matola ([UniTN](https://webapps.unitn.it/du/en/Persona/PER0247884/Curriculum), [GitHub](https://github.com/matteo-d-m))

:mailbox: matteo [dot] dematola [at] unitn [dot] it