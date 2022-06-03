# Merck - Corning Data Science Workshop

# Introduction 
As data project mature, data scientists may need make their functions work on
new data, use them in broader use cases and with other collaborators. These challenges require them to build packages
that works with other people and tools. 

In this workshop we'll look at how to create functions with docstrings that helps new users. 
Then, we'll create a package that others can install. We'll write doc string and comment to help our future self or
other users of our code understand what the code is doing.

Finally, we will make sure the code is performing as expected by writing some tests. Automated tests are useful 
because it serves as a working example of our code and let us check many behaviors quickly.


## Review last year workshop 

## Setup
1. Install your favourite ide such as vscode or pycharm. You can download Pycharm community version for free
   with this (link)[https://www.jetbrains.com/pycharm/download/#section=windows]

2. Install (git)[https://git-scm.com/download/win]

3. Install (anaconda)[https://docs.anaconda.com/anaconda/install/windows/]

4. Clone this repo

5. Create the conda environment by using anaconda prompt by going to Start > Anaconda3 > Anaconda Prompt (Anaconda3)
   Navigating to the folder containing environment.yml, which is where you cloned the repo. 
   ```bash
   cd <full-path/to-environment.yml>
   ```
6. Create a virtual environment

   ```bash
   conda env create -f environment.yml 
   ```
   
   ```bash
   python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
   ```
   Alternatively use the anaconda navigator GUI. Go to Sidebar > Environment > import and import the environment.yml  

## Conda environment in pycharm
At this point 

# Topics
1. docstring and type hinting
2. package
3. testing
   1. assert
   2. approx
   3. pandas approx

# First example
# nlp example: creating data pipeline for contextualizing unstructured text in doctor's note in covid-19 patients

# time-series example: example for data pipeline


| Function                | Task                                                       |
|--------------------|------------------------------------------------------------|
| Detrend Data       | Make the mean of the process signals be zero.              |
| Data Smoothing     | Remove the noise from process signals using a band filter. |
| Data Normalization | Normalize process signals.                                 |
| Remove Outliers    | Detect and remove outliers.                                |

