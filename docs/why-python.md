# Why Python? :snake: :computer:

It is safe to say that modern neuroscience was built on MATLAB and its toolboxes: while it is hard to prove it quantitatively, it is anyone's experience that fMRI studies usually include [SPM](https://www.fil.ion.ucl.ac.uk/spm/software/spm12/)-based analyses, while most M/EEG studies include [EEGLAB](https://sccn.ucsd.edu/eeglab/)- or [Fieldtrip](https://www.fieldtriptoolbox.org/)-based analyses. People that are currently between the late-doctoral and associate-professor stages have learned to code in MATLAB &mdash; and teach MATLAB to their students. 

MATLAB's popularity across the neuroscience community can be safely traced to the two main features of this programing language: 

- **Readability:** compared to languages that were populare before (like [C](https://en.wikipedia.org/wiki/C_(programming_language)) or [Fortran](https://en.wikipedia.org/wiki/Fortran)), MATLAB is easier to read and write
- **Matrix-friendliness:** MATLAB makes it easy to work with matrices, and neuroscience data are usually just that. For example, behavioural data are usually a table with one row per subject and one column per variable, while EEG data are matrices with one row per channel and one column per timepoint

These features are probably the reason why the developers of SPM, EEGLAB or Fieldtrip chose to write their tools in MATLAB, and the very existence of those tools is the main reason why the neuroscience community has adopted MATLAB between the 1990s and 2010s. However, the growth of Python and of the [open science](https://forrt.org/glossary/english/open_science/) movement are slowly undermining MATLAB's primacy. Once again, it is hard to gather quantitative data about the spread of one or another programming language, but it is anyone's experience that an increasing number of neuroscience researchers are transitioning to Python. Today it is increasingly easy to find high-quality Python-based neuroscience tools &mdash; for example, [MNE-Python](https://mne.tools/stable/index.html) for M/EEG and [Nilearn](https://nilearn.github.io/stable/index.html) for MRI. As an example of this trend, CIMeC's doctoral school has stopped offering MATLAB training and has introduced [a compulsory 32-hourse Python course](https://phd.unitn.it/alfresco/download/workspace/SpacesStore/a8180488-fa30-4a39-9804-88fa303a39b6/2025-2026%20Student%20Handbook.pdf) for all new students starting 2025. 

Python has all that MATLAB has, plus something more:

- **High readability:** once you have gained some familiarity, reading (and writing) Python is almost like reading (and writing) plain English
- **Matrix-friendliness:** while Python does not have built-in tools to work easily with matrices, the [NumPy](https://numpy.org/) library does
- **Accessibility:** Python is free and open source (FOS), meaning that anyone can install it and use it without paying a license 
- **Very vast ecosystem:** because Python is FOS, anyone can use it to build new tools. Therefore, people have developed a state-of-the-art Python library for almost anything, from advanced statistics (e.g., [statsmodels](https://www.statsmodels.org/stable/index.html)) to tracking animal movement (e.g., [DeepLabCut](https://deeplabcut.github.io/DeepLabCut/README.html)) and working with databases (e.g., [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)). Modern artificial intelligence is largely built on Python, which is the basis for the two most common deep learning libraries ([PyTorch](https://pytorch.org/) and [TensorFlow](https://www.tensorflow.org/))  
- **Easy integration with reproducibility tools** (see [Using Environments or Containers](./good-programming-practices.md))
- **Easy integration with web technologies** through tools like [Flask](https://flask.palletsprojects.com/en/stable/) or [Django](https://www.djangoproject.com/)

For these reasons, using Python makes a lot of sense in 2025/26. The following quote from [Freeman (2015)](https://www.sciencedirect.com/science/article/pii/S0959438815000756) summarizes these points with more authority than I could have: 

_"Although Matlab is likely the most widely used platform among neuroscientists today, it is hard to recommend as a primary analysis tool in a future of open and collaborative science. User-developed Matlab code can be shared, but Matlab itself is closed-source and expensive. Although easy to use for beginners, and perhaps useful for educational purposes, Matlab has limited or clunky support for distributed computing, or even more basic modern features like functional and object-oriented programming and continuous automated testing. These crucial features make software easier to maintain, test, collaborate on, share, and integrate with other services, especially web-based ones. More fundamentally, **as we look toward a future where research and data are to be publicly shared, it seems inappropriate to allow a single, for-profit entity to effectively tax the reproducibility of results &mdash; much in the same way for-profit journals tax the distribution of knowledge**. Finally, **outside of niche applications, Matlab is much less widely used in industry data science; if we want to train students to succeed within and outside academia, we should teach them more than just Matlab**"_.

# Contacts

For questions or comments, you can contact: 

:question: Matteo De Matola ([UniTN](https://webapps.unitn.it/du/en/Persona/PER0247884/Curriculum), [GitHub](https://github.com/matteo-d-m))

:mailbox: matteo [dot] dematola [at] unitn [dot] it