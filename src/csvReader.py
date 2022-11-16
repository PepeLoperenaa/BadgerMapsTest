import csv
from datetime import datetime
from dateutil.rrule import rrule, DAILY
import re

filename = "../files/testFile.csv"
rows = []


def open_csv2(file_name):
    with open(file_name, encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            rows.append(row)
            flag = False
            for cell in row:
                if cell == 'Street' and not flag:
                    flag = True
                    print("Missing Street")
                elif cell == 'Zip' and not flag:
                    flag = True
                    print("Missing Zip")
                elif cell == 'City' and not flag:
                    flag = True
                    print("Missing City")
                elif cell == 'Last Check-in Date' and not flag:
                    flag = True
                    print("Missing Last Check-in Date")
                elif cell == 'Company' and not flag:
                    flag = True
                    print("Missing Company")
                elif cell == ' ' and flag:
                    return False
        print(rows)
    return True



def earliest_check_in_date():  # Iterate through list and get the earliest date
    for row in rows:
        if re.match(r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}', row):
            print(row, 'is a date')

    '''
    number = 0
    for row in rows:
        date = datetime.strptime(rows[number][6], '%d/%m/%Y')  # works but cannot iterate on it.
        number += 1
        for d in rrule(DAILY, dtstart=date, until=date):
            print(d.strftime('%d/%m/%Y'))
    '''


def lastest_check_in_date():  # Iterate through list and get the latest date
    number = 0
    for row in rows:
        print(rows[number][6])
        number += 1


def customer_full_names():  # Iterate from the whole list and concatenate value[0][1] in every record.
    number = 0
    rows.sort()  # Sort the list alphabetically.
    for row in rows:
        fname = rows[number][0]
        lname = rows[number][1]
        number += 1
        full_name = fname + " " + lname
        print(full_name)


def companies_users_jobs():  # get jobs from the clients. Need to sort alphabetically.
    number = 0
    rows[7].sort()
    for row in rows:
        print(rows[number][7])
        number += 1


open_csv2(filename)
# customer_full_names()
# companies_users_jobs()
# earliest_check_in_date()


# Need to check that every csv file contains  Street, Zip, City, Last Check-in Date and CompanyCheck

'''
It is recommended to log exceptions in case that a required field is empty for that row but the rest of the file is still processed.
It is recommended to log an exception in case a row contains less fields than expected but the rest of the file is still processed.
It is recommended to log an exception in case a row does not contain any data but the rest of the file is still processed.
'''
