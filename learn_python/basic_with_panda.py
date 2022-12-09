from datetime import datetime
import calendar
import boto3
from pandas import *
"""
Function: Can do something. You can get some job done
"""

client = boto3.client('ses')


# How to write a python function

def add(a, b):

    c = a + b

    print(c)
    name = "John"
    school = 'Izaan School'
    print(school)

    # Fency way to print
    print("My Name: {}, {}".format(name, school))

    a = 3
    print(type(a))

    print("name varaible time: {}, school variable type: {}".format(type(name), type(school)))


def students_info():
    students = [ "Foysal" , "Shamim", "Mohiuddin", "Masud", 22]

    print(students)
    print(type(students))

    return students


def send_greetings():
    email_list = get_email_list()
    current_day = get_current_day()

    # if current day is Friday send student a greetings
    # current_day == 'Friday'  - True or False
    # Thursday == Friday --> False
    # Wed == Fri --> False Tue == Fri --> False Mon == Fri --> False

    if current_day == 'Thursday':
        send_email_by_ses()
    else:
        print("Sorry cant send email, today is " + current_day)


def get_email_list():
    """
    1. List of students - Email
    2. Send students good thoughts in every Friday at 5:30 PM

    :return:
    """
    students_email_list = [
        'mr2chowd@uwaterloo.ca','bahjatkhan2002@gmail.com',
        'Rahmanmdm16@gmail.com', 'taha20jibril@gmail.com',
        'adeelmahmood125@gmail.com', 'Leonsubhan@outlook.com',
        'sreza30th@gmail.com'
    ]
    return students_email_list

def csv_reader():
    # reading CSV file
    data = read_csv("data.csv")
    # username,email,status,billing-active,has-2fa,has-sso,userid,fullname,displayname,expiration-timestamp
    # converting column data to list
    name = data['name'].tolist()
    email = data['email'].tolist()

def get_current_day():
    # get current datetime
    dt = datetime.now()
    print('Datetime is:', dt)

    # # weekday (Monday =0 Sunday=6)
    # print('Weekday Number:', dt.weekday())
    #
    # # isoweekday(Monday =1 Sunday=6)
    # print('ISO Weekday Number:', dt.isoweekday())
    #
    # # get weekday name
    # print('Weekday Name:', dt.strftime('%A'))

    # get day name
    current_day = calendar.day_name[dt.weekday()]
    print('Weekday name is:', current_day)
    return current_day


def send_email_by_ses():
    # create a connection object to use aws services.
    #
    #students_email_list = get_email_list()
    # List - Or a data structure
    # 1. How to create the data structure
    # 2. How to insert data into a list?
    # 3. How to update data in a list?
    # 4. How to get the data from a list?
    # 5. How to delete a data from a list?
    # Write original, good code to send folks email

    # for temp_contaianer in target/source
    #    #consumeer
    #    print(temp_contaianer)
    """
    to = info@izaan.io
    from = anyone
    
    """
    # reading CSV file
    data = read_csv("data2.csv")
    # username,email,status,billing-active,has-2fa,has-sso,userid,fullname,displayname,expiration-timestamp
    # converting column data to list
    #name = data['name'].tolist()
    students_email_list = data['email'].tolist()

    for temp_container in students_email_list:
        user_name = temp_container.split('@')[0] # [mr2chowd, uwaterloo.ca]
        message = 'Hi {}, Wishing you a very good day'.format(user_name)
        ses_send(temp_container, message)


def ses_send(email, message):
    response = client.send_email(
        Source='info@izaan.io',
        Destination={
            'ToAddresses': [
                email,
            ]
        },
        Message={
            'Subject': {
                'Data': 'Greetings from Izaan School!!!'
            },
            'Body': {
                'Text': {
                    'Data': message
                },
            }
        },
        ReplyToAddresses=[
            'info@izaan.io',
        ]
    )

# def main():
#     send_greetings()
#
#
# if __name__ == "__main__":
#     #get_studnets_name()
#     main()


send_greetings()

