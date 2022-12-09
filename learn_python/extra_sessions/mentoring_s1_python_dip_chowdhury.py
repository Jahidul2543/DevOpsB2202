
# Variables
# A variable is simply a name to which a value can be assigned.

# Variables allow us to give meaningful names to data.

# The simplest way to assign a value to a variable is through the = operator.


# A big advantage of variables is that they allow us to store data so that we can use it later to perform operations in the code.

# Variables are mutable. Hence, the value of a variable can always be updated or replaced.

print(8/10)

var1=8 
var2= 10 

print(var1/var2)

# How to write exponential in python

print(4**2)

print(18%7)

#lets say you start with 100 buck, at 10 percent interest how much is your net worth 
# How much is your $100 worth after 7 years?
capital=100
interest_rate=10

net_worth=100*(1.1**7)
print(net_worth)

# Naming Convention
# There are certain rules we have to follow when picking the name for a variable:

# The name can start with an upper or lower case alphabet.

# For example, you can define your income variable as Income or income, both are valid.

# All the names are case sensitive.

# For example, Income and income are two different variables and not one.

# A number can appear in the name, but not at the beginning.

# For example, 12income is not a valid name but income12 or in12come are valid.

# The _ character can appear anywhere in the name.

# For example, _income or income_ are valid names.

# Spaces are not allowed. Instead, we must use snake_case to make variable names readable.

# For example, monthly_income is a valid name.

# The name of the variable should be something meaningful that describes the value it holds, instead of being random characters.
# For example, inc or even income would not give any useful information but names like weekly_income, monthly_income, or annual_income explain the purpose of our defined variable



############ BUILT IN FUNCTION TYPE#####################
print(type(net_worth))

x="this is area"
y=True
print(type(x))
print(type(y))

###Example of different print features 
savings = 100
growth_multiplier = 1.1


# Assign product of growth_multiplier and savings to year1
year1=growth_multiplier*savings
year2=growth_multiplier*year1

# print("my net asset in the end of year 1 is going to {}".format(year1))
year1=int(year1)

print(f"my net asset in end of year 1 is {year1} and year2 is {year2}")

# Assign sum of desc and desc to doubledesc

var1='interest'
# var2=var1*var1
# print(var2)

######## Definition
# The data type of an item defines the type and range of values that item can have.

# The concept of data types can be found in the real world. 
# There are numbers, alphabets, characters, etc., that all have unique properties due to their classification.

# Such a classification is also made in many programming languages, including Python.

# Python’s Data Types
# Unlike many other languages, 
# Python does not place a strong emphasis on defining the data type of an object, which makes coding much simpler. 
# The language provides three main data types:

#######Common Data types List but not all of them listed here

#1) Numbers
#2Boolean
#3) String
#4) List
#5) Tuple
#6) Set
#7) Dictionary
#8) Dataframe

fam=[1.7,1.68,1.13,1.89]

sister=1.7 
my_dad=1.68

fam=["sister",1.7,"dad",1.68,"mother",1.13,"me",1.89]

## so which of the following ways do are right for creating a list? 
A=[1, 3, 4, 2] 
B=[[1, 2, 3], [4, 5, 7]] 
print(type(B))
C= [1 + 2, "a" * 5, 3]  

# Slicing is the process of obtaining a portion (substring) of a string by using its indices.

# Given a string, we can use the following template to slice it and obtain a substring:

# string[start:end] 
# start is the index from where we want the substring to start.
# end is the index where we want our substring to end.
# The character at the end index in the string, will not be included in the substring obtained through this method.



#INDEXING AND LIST SUBSETTING 
fam=["sister",1.7,"dad",1.68,"mother",1.13,"me",1.89]
print(fam[-2])
print(fam[6])
print(fam[-1])

##CONCEPT : LIST SLICING 
NEW_FAM= fam[3:5]
print(NEW_FAM)

NEW_FAM= fam[4:6]
print(NEW_FAM)

fam=["sister",1.7,"dad",1.68,"mother",1.13,"me",1.89]
NEW_FAM= fam[6:]
print(NEW_FAM)

NEW_FAM= fam[:5]
print(NEW_FAM)

###ANOTHER SUBSETTIG EXAMPLE 

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

eat_sleeping_are=areas[3]+areas[7]

print(areas[3]+areas[7])

############DATA TYPE TUPLE AND ITS IMMUTABILITY ######################

# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and 
# Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.
tuples=(2,5.5,6.6)

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# Example
# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple items can be of any data type:

# Example
# String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
##################
x = ["a", "b", "c", "d"]

x[0]="s"

# print(x)

x = ["a", "b", "c", "d"]
x[2:3]=["s","t"]
print(x)

x = ["a", "b", "c", "d"]
x[2:]=[1,[1,5]]
print(x)

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
new_washroom_area=10.5
areas[-1]=new_washroom_area

print(areas)

x=["a","b","c","d"]
new_list=["e","f"]+x
print(new_list)

########### HOW DO YOU DELETE AN ELEMENT FROM LIST##############

# # del(x[1])
# print(x)

x=["a","b","c","d"]
del(x[1:])
print(x)

#############Functions#############

var="hey"

type(var)

#######EXAMPLES OF SOME BUILTIN FUNCTIONS###############

fam=[1.7,1.68,1.13,1.89]

#########WHO IS THE TALLEST and shortest IN MY FAMILY###############???????????????

print(max(fam))

print(min(fam))

############ROUND FUNCTIONS######################
print(round(1.69,1))
print(round(1.69,0))
print(round(1.69))

# help(round)

# help(type)

#######SORTED FUNCTION WITH EXAMPLE###############
# Create lists first and second

first=[11.25,18.0,20.0]
second= [10.75,9.5]
full=first+second
print(full)

# Sort full in descending order: full_sorted
full_sorted=sorted(full,reverse=True)
print(full_sorted)

full_sorted=sorted(full)
print(full_sorted)

######################################################################
def my_first_function(item,lyst):
    index_number=lyst.index(item)
    print(f"the index number of your given {item} is {index_number}")
###################################################################
list1=["salmon","sashimi","salmon","sushi","salmon"]

my_first_function("sashimi",["salmon","sashimi","salmon","sushi"])

wali=["salmon","sashimi","salmon","sushi","salmon"]

def second_function(fish,list_of_fish):
    total_count=list_of_fish.count(fish)
    print(f"the count of your given {fish} is {total_count}")

second_function("salmon",wali)

##################WHAT ARE METHODS########################

place="poolhouse"

place_up=place.upper()
print(place_up)

######counting strings#######

print(place.count("o"))

######capitalize method###########

print(place.capitalize())

###########replace method############

# name="liza"
# name1=name.replace("z","p")
# print(name)

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas.append(11)
areas.append(15.45)
print(areas)

##############reverse##############
areas.reverse()
print(areas)

########DICTIONARY################
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan","albania","algeria"]
ind_alb=countries.index("albania")
print(ind_alb)
print(pop[1])

world={"afghanistan":30.55,"albania":2.77,"algeria":39.21}

print(world.keys())

print(world["algeria"])

world["Bangladesh"]=200


world["Bangladesh"]=201


# del world['Bangladesh']

world.pop('Bangladesh',None)

print(world)

print(world)


############keys are immutable#############

# Complex Numbers

# Python also supports complex numbers, or numbers made up of a real and an imaginary part.

# Just like the print() statement is used to print values, complex() is used to create complex numbers.

# It requires two values. The first one will be the real part of the complex number, while the second value will be the imaginary part.

# Here’s the template for making a complex number:

# complex(real, imaginary)
print(complex(10, 20))  # Represents the complex number (10 + 20j)
print(complex(2.5, -18.2))  # Represents the complex number (2.5 - 18.2j)

complex_1 = complex(0, 2)
complex_2 = complex(2, 0)
print(complex_1)
print(complex_2)












