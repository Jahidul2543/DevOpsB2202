def old_raise_to_power(number,power):
    value= number**power
    return print(value)
# old_raise_to_power(2,3)

raise_to_power=lambda number,power:print(number**power)
# raise_to_power(2,3)

#####Example 2 

#define echo word as a lambda functions ::: 
echo_word=lambda word1, echo: word1*echo
result= echo_word('hey',5)
# print(result)
#define echo word as a lambda functions ::: 
echo_word=lambda word1, echo: word1*echo
result= echo_word('swing',2)
# print(result)

# Example:4 SHOWING THE MAP FUNCTION AS WELL 

nums=[48,6,9,21,1]

square_all=map(lambda x: x**2,nums)

################this is a map object, so to get the list we need to unpack it, i.e with pythons built in list function

# print(list(square_all))


##########another example with FILTER to clarify###############

candidates = ['mohyminur', 'taha', 'foysal','wali','mohiuddin','adeel']
result=filter(lambda x: len(x)>5,candidates)
# print(list(result))


#####################DATAFRAMES#########################

#####MANUAL WAY TO CONVERT A LIST TO DICTIONARY AND THEN TO DATAFRAME 
import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict= {'country': names, 'drives_right':dr, 'cars_per_cap':cpc}
# print(cars_dict)
cars = pd.DataFrame(cars_dict)

row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index=row_labels
# print(cars)

# Import the cars.csv data: cars
path="C:\Documents\Teaching courses\Devops\Python classes\Basics - mentoring session 1\Solutions\cars.csv"
car=pd.read_csv(path,index_col=0)
# print(cars)
# print(car[["country"]])
# print(car[["country","drives_right"]])

# print(car[0:3])

#######loc and iloc concepts##########
# # print(cars.iloc[0:4,:1])
# # .loc
# print(cars.loc[["MOR"],["drives_right"]])

# print(cars.loc[["RU","MOR"],["country","drives_right"]])

# # Print out drives_right column as DataFrame
# print(cars.loc[:,["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame
# print(cars.loc[:,["cars_per_cap","drives_right"]])



################COMPARATORS#############################
# print(2 < 3 )

# print(2 == 3 )

# print(2 <= 3 )

# print(2 >= 3 )


# print("carl" < "chris")

# x = 16
# print(x > 5 and x < 15)
# y=6
# print(y < 7 or y > 13)
# print(car)

cpc=cars["cars_per_cap"]
many_cars=cpc>500
# print(cars[many_cars])

################# ARRAYSSSSSSS ##########
####showing usefulness of arrays##########
fam=[1.7,1.68,1.13,1.89]
# print(fam>1.6)
# boolean=[]
# for x in fam:
#     if x > 1.6: 
#         boolean.append(True)
#     else: 
#         boolean.append(False)
# print(boolean)
import numpy as np 
np_array=np.array(fam)
# print(np_array>1.6)

############ CONTROL FLOW #######################

# if condition :
#     expression


z = 4
# if z % 2 == 0 : # True
    # print("z is even")

########ELIF STATEMENTS ################
z = 7
if z % 2 == 0 :
    print("z is divisible by 2") # True
elif z % 3 == 0 :
    print("z is divisible by 3") # Never reached
else: 
    print("z is not divisable by 2 or 3")

##Example 2: 
area = 16.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")

# Example 3

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area >= 14 :
    print("big place!")

# The syntax of while loop is:

# while condition:
#     # body of while loop

# A while loop evaluates the condition
# If the condition evaluates to True, the code inside the while loop is executed.
# condition is evaluated again.
# This process continues until the condition is False.
# When condition evaluates to False, the loop stops.

########PROBLEM WORK FLOW#############
# Numerically calculating model
# "repeating action until condition is met"

# Example
# Error starts at 50
# Divide error by 4 on every run
# Continue until error no longer > 1
# error = 50 

# while error > 1: 
#     error= error/5
#     # print(error)


# x=1 

# while x < 4: 
#     # print(x)
#     x=x+3

######SOOOOOO FOR LOOOOP AGAIN #########################

# for variable in sequence: 
#     expression = "write your task"

fam= [1.73, 1.68, 1.71, 1.89]

# print(fam[0])
# print(fam[1])
# print(fam[2])
# print(fam[3])

for x in fam: 
    print(x)
fam= [1.73, 1.68, 1.71, 1.89]
# x=enumerate(fam)
# print(next(x))
# print(next(x))
# print(next(x))

# index= [0,1,2,3,4,5]

# for index,height in enumerate(fam): 
#     print(f"index for first iteration object is {index} and the height is {height}")


######simple syntax for range function################
# range(start, end, step)

# for i in range(1,11):
#     print(i)

######another example of range
for i in range(1, 11):  # A sequence from 1 to 10
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")

# house list of lists
house = [["hallway", 11.25,"MYHOUSE"], 
         ["kitchen", 18.0,"MY2222HOUSE"], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
for x in house: 
    print(f"the {x[0]} is {x[1]} square meteres ")
# HOLL=["hallway", 11.25]
# print(HOLL[0])

########DICTIONARY LOOOPING#################

world = { "afghanistan":30.55,
"albania":2.77,
"algeria":39.21 }

print(world.items())

for key,value in world.items(): 
    print(key + "---" + str(value))



# [('afghanistan', 30.55), ('albania', 2.77), ('algeria', 39.21)]

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }

for key,value in europe.items(): 
    print(f"the capital of {key} is {value}")




















