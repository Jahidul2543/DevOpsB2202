from datetime import datetime
import calendar


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
    students_email_list = get_email_list()
    # Write original, good code to send folks email
    message = 'Hi {}, Wishing you a very good day'.format(students_email_list[0])
    print()


# def main():
#     send_greetings()
#
#
# if __name__ == "__main__":
#     #get_studnets_name()
#     main()

send_greetings()