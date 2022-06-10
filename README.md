# Deep-Learning-Analysis-Tool
Contribution: Safety concept for applied deep learning applications
-------------------------------------------------------------------

This is the introduction to the tool that deals with the analysis of the output (accuracies)
of the neural network used.

To start with using the tool, first you should insert the data of Batch 5 in the appropriate folder. 
The reason why there is no data is because of avoiding long time ranges of downloading this project.

At the beginning, you should first let the validation pipeline run through, which saves 
all accuracy values for the data records considered in batch 5.
From now on, the file with all accuracies will be used permanently to reduce the loading time of the analysis tool. 
You can find it as a .json file in the project folder.

After runing the Abgabe.py, which is the main program of this work, the Welcome Display will be printed out.
First, an interface will be displayed, which you must confirm with enter. 
You will then be asked which of the 3 described functions of the analysis tool 
you would like to use.

The first function shows the accuracy of a data set you want to analyze with the tool. 
You decide which dataset you want to look at more closely (or which traffic sign).

The second function let you set a limit and shows you all data sets whose accuracy 
values are below the set threshold. 
In addition, a bar chart will be displayed to visualize all values, with which you can immediately 
see how the individual data sets relate to your limit value.

By navigating to the third function, you can compare a data set you have explicitly requested 
with your set threshold.
