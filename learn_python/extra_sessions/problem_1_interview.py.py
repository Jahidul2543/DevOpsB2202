####Question 1 ########

###Step 1
#Look the raw_input variable with bunch of raw data that needs to be processed: 

# Step 2 
# create a function where you will be using 
# control-flow that can process the sizeInBytes
# column inputs to something like that is similar to output shown below in example: 

#Step 3 Convert the raw input into a format of your choice, maybe data type list or dataframe will be easier to handle and manipulate

#Step 4: 

    # Group by document.createdBy

    # Sort the groups using document.createdBy ascending, case insensitive

    #     Sort each sub list of documents by document.createdTime ascending

    # Format the output of document.size to be a more friendly format. Ex.  50 mb, 900 k, 342 bytes, etc...

    # Format the dates using the format: yyyy-MM-dd

    # Format the output of document.description such that

    #     - no more than the first 25 characters of the description are displayed

    #     - don't truncate any words unless the first word is longer than 25 characters

    #     - display "..." at the end of the description to indicate that it has been truncated

    #           (these three characters do not count as part of the 25 character limit)



## Prints a report of the list of documents in the following format:

#         Example:

#           Andy Andrews

#              "Bobby Timmons Biography","An exhaustive look at the ...",233 mb,2013-05-09,2013-05-14

#              "Apple Sauce","Study of apple sauces.”,87 gb,2013-05-10,2013-05-10

#              "Zed","All matters, A to Zed”,924 k,2013-05-12,2013-05-12

#           Janet Smith

#              "Xray","How the Xray shows your ...",48 mb,2010-10-22,2010-12-02

#              "Computers","Inventory list of ...",423 bytes,2013-03-01,2013-02-17

#      
raw_input = [

    {

        'name':'Computers',

        'description': 'Inventory list of unregistered equipments',

        'createdBy':'Janet Smith',

        'lastModifiedBy': 'Smith Janet',

        'sizeInBytes': 423,

        'createdTime':1362114000,

        'modifiedTime':1361077200

    },

    {

        'name':'Apple Sauce',

        'description': 'Study of apple sauces.',

        'createdBy':'Andy Andrews',

        'lastModifiedBy': 'Andy Andrews',

        'sizeInBytes': 93415538688,

        'createdTime':1368158400,

        'modifiedTime':1368158400

    },

    {

        'name':'Zed',

        'description': 'All matters, A to Zed',

        'createdBy':'Andy Andrews',

        'lastModifiedBy': 'Andy Andrews',

        'sizeInBytes': 946176,

        'createdTime':1368331200,

        'modifiedTime':1368331200

    },

    {

        'name':'Xray',

        'description': 'How the Xray shows your health',

        'createdBy':'Janet Smith',

        'lastModifiedBy': 'Smith Janet',

        'sizeInBytes': 50331648,

        'createdTime':1287720000,

        'modifiedTime':1291266000

    },

    {

        'name':'Bobby Timmons Biography',

        'description': 'An exhaustive look at the funny characters.',

        'createdBy':'Andy Andrews',

        'lastModifiedBy': 'Andy Andrews',

        'sizeInBytes': 244318208,

        'createdTime':1368072000,

        'modifiedTime':1368504000

    }

]