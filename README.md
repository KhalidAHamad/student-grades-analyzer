## Introduction and motivation

Since entering university, I have noticed that some of my colleagues are struggling every time a lecturer puts out our marks because they have to go through large excel files just trying to compare their marks with the marks of other students. Thus, I made this program to ease the process for my classmates and automate the analysis for my lecturers as well.

## Getting started

### Preconditions
This is a very basic app written in Python3.8 that is capable of analyzing 
*CSV*/*Excel* files that fulfill the following conditions:
- The file has 2 columns at least with the names: `matric number` and `mark`.
- The file does NOT contain any lines before the column names (you can refer
  to the images below for further explanation).

### Installation
- Python version: 3.8.0
- You can clone or download this repository and then install the required
packages.
- The list of packages used in this app could be found in the requirements.txt
file and can be installed using pip.

### Using the app
Once you select your file, a compact report will be displayed on the screen.
The report will contain the following information:
- The average (mean) score.
- The median score.
- The lowest mark.
- The highest mark.
- A list of students' matric (matriculation) numbers who scored the highest mark.

After that, you will be given the option to see a histogram illustrating the
marks distribution. Finally, after you close the chart and Tkinter window (if 
you do not know what I mean by the latter, do not worry, it is illustrated
below in pictures) you will be given the option to save the report above
without the chart to a text file.

## Illustrations

##### The program is expected to be used with a file structure similar to this
<img src="images/works.png">

---

##### It will NOT work with the following structure. (_column names are NOT in the first line_)
<img src="images/doesnt-work.png">

---

##### After you select and open your file, close the Tkinter window (the window in the picture below)
<img src="images/tk-window.png">

---

##### The histogram on the right side and the app running on the left side
<img src="images/hist.png">

## Connect with me
[LinkedIn](https://www.linkedin.com/in/khalidhamad/)
