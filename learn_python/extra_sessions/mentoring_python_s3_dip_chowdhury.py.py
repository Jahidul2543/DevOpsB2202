#############WRITE A NORMAL FUNCTION WITH DEFAULT VALUE############
def power(number,power=2): 
    ###raise the power of the number by power########
    new_value=number ** power

    return print(new_value)

power(5)


###########ARGS##########

def gibber(*args):
    holder=''

    for word in args: 
        holder= holder+word
    
    return print(holder)

gibber("taha"," ","masud")

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# # First call to report_status()
# report_status(name="luke", affiliation="jedi", status="missing")

# # Second call to report_status()
# report_status(name="anakin", affiliation="sith lord", status="deceased")

############lets practice the AWS LAMBDA WITH EVENT TRIGGERS######

import json
import boto3
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # List the buckets
    response = s3.list_buckets()
    print(response)

#########how do we get it in a format we like#####

##any suggestions? 


import json
import boto3
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # List the buckets
    response = s3.list_buckets()
    buckets =[]
    for x in response["Buckets"]:
      print(x)

#################how do we confine it to something even better##########
##lets say extract the name from the dictionary???####

import json
import boto3
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # List the buckets
    response = s3.list_buckets()
    buckets =[]
    for x in response["Buckets"]:
      print(x['Name'])


##########how to create a bucket in s3 using aws lambda##########

import json
import boto3
def lambda_handler(event, context):
    s3=boto3.client('s3')
    response=s3.list_buckets()
    buckets=[]
    for x in response["Buckets"]:
        print(x["Name"])
    
    s3.create_bucket(Bucket="staging2023bucket1")

#######how to upload a file using boto3##########

import boto3 

s3=boto3.client('s3',region_name='us-east-1')

s3.upload_file(Filename="cars.csv",Key="2022/mycars.csv",Bucket="staging2022a66",ExtraArgs={'ACL':'public-read'})










#####The theory 
# A for loop uses an iterator to traverse a sequence, e.g. a range of numbers, 
# 
# the elements of a list, etc. 
# 
# In simple terms, the iterator is a variable that goes through the list.

# The iterator starts from the beginning of the sequence. 
# In each iteration, the iterator updates to the next value in the sequence.

# The loop ends when the iterator reaches the end.

fam = [1.73, 1.68, 1.71, 1.89]

# for x in fam: 
#     # print(x)

##loop over dictionary ####

world = { "afghanistan":30.55,
"albania":2.77,
"algeria":39.21 }

# print(world.items())

# for x,y in world.items():
#     print(f"this is the key {x} and the value of key is {y}" )

a,b,c=("taha","mohiuddin","masud")

# print(a)

###################### start from here#####################
 ####another example of DATAFRAME iteration with for loop:     

import pandas as pd 

cars=pd.read_csv('cars.csv',index_col=0)
#prints the top three rows now

# print(cars.head(3))
#prints the bottom three rows now
# print(cars.tail(3))


######so what kind of data is this##########

# print(type(cars))


############USING FOR LOOP FOR DATAFRAME###############

# for label,row in cars.iterrows():
#     print(label)
#     print(row)

# var=cars.iterrows()
# print(next(var))

#######LETS USE UPPER FUNCTION TO MAKE A NEW COLUMN IN THE DATAFRAME#######
# cars=pd.read_csv('cars.csv',index_col=0)
# for label,row in cars.iterrows():
#     cars.loc[label,"COUNTRY_UPPER"]= row["country"].upper()

# print(cars)

###################creating a new column including datframe apply function#######

# cars["ANYTHING"]=cars["country"].apply(str.upper)

# # print(cars)

# cars.to_csv("anything.csv")


########lets load a EXCEL###########

# cars=pd.read_excel('cars.xlsx',index_col=0)



