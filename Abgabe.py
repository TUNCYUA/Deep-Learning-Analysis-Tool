import matplotlib.pyplot as plt
import numpy as np
import json

#Creating a dict to name all used Batch 5 datasets
class_names = {                                             
    0: "Permissible maximum speed: 20",              
    1: "Permissible maximum speed: 30",        
    2: "Permissible maximum speed: 50",        
    3: "Permissible maximum speed: 60",       
    4: "Permissible maximum speed: 70",      
    5: "Permissible maximum speed: 80",       
    6: "End of the maximum speed limit: 80",       
    7: "Permissible maximum speed: 100",        
    8: "Permissible maximum speed: 120",      
    9: "Overtaking ban vehicles",       
    10: "Overtaking ban for vehicles > 3,5t)",      
    11: "Crossing",     
    12: "Priority road",      
    13: "Give way",      
    14: "Stop sign",      
    15: "Vehicle ban",      
    16: "Ban for vehicles more than 3,5t",     
    17: "Drive-through ban",      
    18: "Danger point",      
    19: "Left turn",      
    20: "Right turn",      
    21: "Double curve",      
    22: "Uneven road surface",      
    23: "Slingshot o. Slippery",     
    24: "Lane narrowed on one side (right)",      
    25: "Work on road",      
    26: "Traffic lights",      
    27: "Pedestrian",      
    28: "Children",      
    29: "Ban bicycle traffic",      
    30: "Danger of snow",      
    31: "Deer crossing",      
    32: "Unlimited speed",      
    33: "Prescribed direction of travel right",
    34: "Prescribed direction of travel left",      
    35: "P. direction of travel straight ahead",      
    36: "P.d. of travel straight ahead or right",      
    37: "P.d. of travel straight ahead or left",      
    38: "Prescribed passing on the right",      
    39: "Prescribed passing on the left",      
    40: "Traffic circle",      
    41: "End overtaking ban vehicle",      
    42: "End overtaking ban for vehicles > 3,5t",      
            }      

#UI-Welcome display is starting
print("Welcome to the work of the topic: Safety concept for applied deep learning applications! Confirm with Enter for the next step!")        
user_input = input()
print("-------------------------------------------------------------------------------------------------------------------\n")
print(" > Do you want to select a class (type of road signs) from which the Accuracy should be issued <x> ? \n") 
print(" > Do you want to set a threshold value? This way you can display all accuracy values that are below your threshold. <y>\n") 
print(" > Or do you want to choose both? This means that a specific type of traffic sign is tested for a limit value <z> ! \n") 
user_input = input("Now make your choice! \n")
print("You have chosen: " + str(user_input))  


def calculate_accuracy():    
    '''Displays accuracy of choosed class'''                                                                 
    user_input = input("What class of traffic signs do you want to look at? \n")            

    if int(user_input) > -1 and int(user_input) < 43:
        print("You have chosen the following class: " + str(user_input))                 

    else:
        print("Invalid input - Please repeat!") 
        return     

    #Using json.load to scan the accuracy-values of the builded dictionary from the .json file
    with open("accuracies.json", "r") as f:
    #f -> json file                                                  
        classacc = json.load(f)                                                                

    print("Accuracy with respect to the considered class (and thus the associated traffic sign) is: " + str(classacc[user_input]*100))         
    return

def plot_graph():  
    '''#Displays the accuracies which are below the treshold set'''                                                                         
    user_input = input("Please set your threshold in %! \n")  

    #Condition for accepting the user input 
    if float(user_input) >= 0 and float(user_input) <= 100:                                 
        print("Your threshold is: " + str(user_input))  
        #Loading accuracy values from dict .json file into variable classacc                 
        with open("accuracies.json", "r") as f:                                              
            classacc = json.load(f) 

        #For-loop runs trough all contents of the .json file while counting up x
        for x, value in classacc.items():
            #Displaying only if value is smaller than treshold                                                   
            if value*100 < float(user_input):
                #Printing the element with its accuracy                                               
                print(x,value*100)                                                          

        #Plot-accessing the class number with .keys & the accuracy value of an key with .values                                                                                                           
        plt.stem(list(classacc.keys()), np.array(list(classacc.values())) * 100) 
        #Displaying the treshold from the user input                  
        plt.axhline(y = float(user_input), color ="red", linestyle ="-")
        #Printing the names of the traffic signs defined in the dictionary class_names                            
        plt.xticks(plt.xticks()[0], [class_names[int(k)] for k in classacc.keys()], rotation=90)                
        plt.subplots_adjust(left=0.05, bottom=0.4, right=0.95, top=0.95)
        plt.show()                                                              
                                                                     
    else:
       print("Invalid input - Please repeat!")  

def treshold_check():     
    '''Proves if the accuracy of the choosed class is below or above the choosed treshold'''                                                                  
    user_input1 = input("So you want to determine both parameters? Please define first the class and therefore the traffic sign you want to check! \n")
    user_input2 = input("Now also define the corresponding threshold value in %! \n")

    if int(user_input1) > -1 and int(user_input1) < 43:                     
        print("You have chosen class: " + str(user_input1))                 
    else:
        print("Invalid input - Please repeat!")
        return                                                                 

    if float(user_input2) >= 0 and float(user_input2) <= 100:
        print("And the threshold: " + str(user_input2)) 
    else:
        print("Invalid input - Please repeat!")
        return

    with open("accuracies.json", "r") as f:                   
        classacc = json.load(f)
     
    value = classacc[user_input1]                                            
    if value*100 < float(user_input2): 
        print("Attention, the determined accuracy regarding the selected class is below the threshold value!: " + str(value*100))
    else: 
        print("The accuracy of the class is: " + str(value*100))             
        print("It is therefore above your threshold!")                                                      

#Calling the main 3 functions of this code
if user_input == "x":                                                        
    calculate_accuracy()            
elif user_input == "y":
    plot_graph()
elif user_input == "z":
    treshold_check()