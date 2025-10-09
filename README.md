# **Brain Stimulation & Multimodal Electrophysiological Recording &mdash; Hands-on!**

This repository contains Python code for the hands-on TMS-EEG preprocessing activity offered as part of the [Brain Stimulation & Multimodal Electrophysiological Recording](https://unitn.coursecatalogue.cineca.it/insegnamenti/2025/50512_653501_96292/2011/50513/10168?annoOrdinamento=2011&coorte=2024) course, taught by prof. Carlo Miniussi and prof. Paolo Belardinelli at the [Master's Degree in Cognitive Science](https://corsi.unitn.it/en/cognitive-science), University of Trento (academic year 2025/2026).

The repository was created and is maintained by the course tutor Matteo De Matola.

```bash
root/
├── docs/                      # text documents with supplementary materials & tutorials
├── files/                     # supplementary files (e.g., images)
├── README.md                  # the file you are reading, the information you need
├── brainstim-multimodal.yml   # installation file (see below)
└── pipeline.ipynb             # the actual python code for the hands-on activity
```

## Jump to

- [General facts](#general-facts)
- [For the exam](#for-the-exam)
    - [Attendance rules for the hands-on activity](#attendance-rules-for-the-hands-on-activity)
    - [Evaluation criteria for the hands-on activity](#evaluation-criteria-for-the-hands-on-activity)
- [Calendar](#calendar)
- [Installation instructions](#installation-instructions)
- [Contacts](#contacts)

## General facts

All the code is contained in a single Jupyter Notebook called `pipeline.ipynb`. A [Jupyter Notebook](https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb) is an interactive document that contains a mix of static text and executable code. The static text can be enriched with mathematical formulas and media such as images or videos, making notebooks a powerful tool to write and present code with explanations.

The goal of the hands-on activity is to progressively populate `pipeline.ipynb` with all the basic steps of a TMS-EEG preprocessing pipeline, complementing the actual code with explanations about what it does, its scientific goal and its effects on the data (for example: _"The following code applies a low-pass filter to the data to attenuate high-frequency noise. As can be seen in the plots, the filter does this and that to the signal"_). 

The hands-on activities will unfold over a series of in-person meetings with the course tutor [Matteo De Matola](https://webapps.unitn.it/du/en/Persona/PER0247884/Curriculum). The meetings will come in pairs: a _pre_ meeting and a corresponding _post_ meeting, interleaved by home assignments for the students. The home assignments will count for the final exam if students choose to take the exam under Option A (see [For the exam](#for-the-exam)).

- In the _pre_ meeting, Matteo will introduce a set of preprocessing steps, their scientific goal and their Python implementations. This will help revise the theory introduced by prof. Belardinelli and translate it into practice. Students will leave the meeting with working Python code provided by Matteo, but they will be free to write their own implementation should they have Python skills at the appropriate level. In this case, the appropriateness of their implementation will be evaluated for the exam
- At home, the students will run the code presented during the _pre_ meeting and comment extensively on its outputs, applying the concepts that they have learned in class. In this phase, students will work on their own copy of `pipeline.ipynb`, writing their comments in the appropriate text cells in an academic style. Students are expected to work independently, but Matteo will be available via email to help them solve technical problems or clarify any doubts. At the end of their work, students will submit their own copy of `pipeline.ipynb`, complete with comments, by 09:00 AM on the day of the _post_ meeting (that is, if the _post_ meeting is on Monday, submit your work by 09:00 AM on Monday)
- In the _post_ meeting, Matteo will provide the students with the correct comments and lead an in-depth discussion of any issues (technical or theoretical) that may arise. After the _post_ meeting, Matteo will update this repository with his own version of `pipeline.ipynb`, containing the correct comments for future reference and comparison

## For the exam

As explained in class, students that attend the Brain Stimulation & Multimodal Electrophysiological Recording course have two options: 

1. **Option A:** carry out two practical activities &mdash; one for Miniussi's part, one for Belardinelli's part:
    - For Miniussi's part (Brain Stimulation), write a grant proposal for a study involving brain stimulation and multimodal electrophysiological recording. This part is not addressed by the present repository
    - For Belardinelli's part, attend the hands-on preprocessing activity described in this repository and carry out the related assignments. Assignments for the hands-on activity must be submitted to Matteo as described above (that is, by 09:00 AM on the day of _post_ meetings). 
2. **Option B:** take an oral exam about the whole program in any exam session

For students that choose Option A, the final grade will be the `{average/weighted average}` of the two grades (Miniussi's and Belardinelli's).

### Attendance rules for the hands-on activity

Everyone is free to attend the meetings, meaning that attendance does not imply a commitment to carrying out the assignments and respect the deadlines. 

However, students that want to take the exam under Option A **must** attend the _pre-post_ meetings and they **must** submit all home assignments by the deadline. 

A maximum of one absence to the meetings will be tolerated (though discouraged). Late submissions will not be tolerated in the absence of a documented cause such as debilitating illness or other accidents. 

### Evaluation criteria for the hands-on activity 

Students that decide to take the exam under Option A will be evaluated for their hands-on activities. Students are not expected to enter the course with advanced coding skills, so their ability to read and write the code will **not** be an evaluation criterion. 

What **will** be evaluated is:

1. **Participation to all _pre_ and _post_ meetings**: 6 points
    - One absence: -2 points (unless the absence is counterbalanced by excellence in the assignments)
2. **Submitting all the assignments by the deadlines**:  8 points
    - Students that miss one deadline lose the chance to take the exam under Option A. Clearly, they can still take the exam under Option B
3. **Mentioning and explaining all the relevant theoretical concepts in the assignments**: maximum 12 points
4. **Clear formal writing**: maximum 4 points  
4. **_Cum laude_ awarded upon reaching 30/30, if one or more of the following conditions are met**: 
    - Continued active participation during _pre_/_post_ meetings
    - Ability to find and explain non-trivial connections between concepts 
    - Ability to write one's own implementations or extend/improve Matteo's
    - Clearly demonstrated interest in the subject, beyond the minimum required  

## **Calendar**

Meetings will be as follows:

0. **Installations check, general Q&As** 
    - dd/mm/yyyy at Place
1. **Basic preprocessing:** rationale, interpolating the pulse artifact, downsampling, filtering 
    - _Pre_ meeting dd/mm/yyyy at Place, _Post_ meeting dd/mm/yyyy at Place 
2. **Independent component analysis (ICA):** rationale, fitting, components selection  
    - _Pre_ meeting dd/mm/yyyy at Place, _Post_ meeting dd/mm/yyyy at Place
3. **Manual artifact rejection:** rationale and execution 
    - _Pre_ meeting dd/mm/yyyy at Place, _Post_ meeting dd/mm/yyyy at Place
4. **Assessing & computing a TEP** 
    - _Pre_ meeting dd/mm/yyyy at Place, _Post_ meeting dd/mm/yyyy at Place

## **Installation instructions**

To participate in the hands-on activities, you will need a laptop with a working Python installation and all the necessary Python-based software like [MNE-Python](https://mne.tools/stable/index.html). To this end, you will need to go through the steps below.

### Option 1: Without using Git

1. Click on [this](https://github.com/vigji/python-cimec-2025/blob/main/docs/python-installation.md) link and follow the instructions until point 1 included (_Install Jupyter in the base environment_) 
2. In this repository, click on the green `Code` button, as in the image below. Once you have done that, click on `Download ZIP`
![Download ZIP](files/where-to-download-zip.png)
3. Once the download is complete, extract the folder in a directory of your choice
4. Open a terminal and run the following code:

```
cd <insert the directory where you have extracted the zipped folder>
conda env create -f brainstim-multimodal.yml
```

### Option 2: Using Git

1. Click on [this](https://github.com/vigji/python-cimec-2025/blob/main/docs/python-installation.md) link and follow the instructions until point 1 included (_Install Jupyter in the base environment_) 
2. In a terminal, run the following code:

```
cd <insert the directory where you want to save this project>
git clone https://github.com/coneco-lab/brainstim-multimodal.git
cd brainstim-multimodal
conda env create -f brainstim-multimodal.yml
```

If you have problems with any of the steps above you are welcome to seek assistance from Matteo, via email or in person. Meeting 0 will be entirely dedicated to this. 

## Contacts

:question: Matteo De Matola ([UniTN](https://webapps.unitn.it/du/en/Persona/PER0247884/Curriculum), [GitHub](https://github.com/matteo-d-m))

:mailbox: matteo [dot] dematola [at] unitn [dot] it