# Deep-Learning-Analysis-Tool
Contribution: Safety concept for applied deep learning applications
-------------------------------------------------------------------

This is the introduction to the tool that deals with the analysis of the output 
of the neural network used.

At the beginning, you should first let the validation pipeline run through, which saves 
all accuracy values ​​​​for the data records considered in batch 5. 
From now on, this will be used permanently to reduce the loading time of the analysis tool. 
You can find this as a .json file in the project folder.

After runing the Abgabe.py, which is the main program of this work, the Welcome Display will be printed out.
First, an interface awaits you, which you must confirm with enter. 
You will then be asked which of the 3 described functions of the analysis tool 
you would like to use.

The first function shows the accuracy you want to determine the neural network. 
You decide which dataset you want to look at more closely or which traffic sign

The second function lets you set a limit and shows you all data sets whose accuracy 
values ​​are below the specified limit. 
In addition, a bar chart is output to visualize all values, with which you can immediately 
see visually how the individual data sets relate to your limit value.

By navigating to the third function, you can compare a data set you have explicitly requested 
with a limit value.
