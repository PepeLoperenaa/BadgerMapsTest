import csv
import datetime as dt

rows = []


def open_csv(file_name):  # opening and storing the csv file in a list.
    with open(file_name, encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)  # delete the header of the csv
        for row in reader:
            rows.append(row)
            flag = False
            for cell in row:  # check if the required fields have the necessary data.
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
                    return False  # if it does not work, return false.
    return True


def convert_date_time():
    dates = []  # get dates in string format
    dates_list = [dt.datetime]  # datatype is datetime
    for row in rows:
        dates.append(row[6])
    full_dates = [x for x in dates if x != '']  # delete records that are empty
    return [dt.datetime.strptime(date, '%d/%m/%Y').date() for date in full_dates]


def earliest_check_in_date():  # Iterate through list and get the earliest date
    min_list = convert_date_time()
    print(min(min_list))


def last_check_in_date():  # Iterate through list and get the latest date
    max_list = convert_date_time()
    print(max(max_list))


def customer_full_names():  # Iterate from the whole list and concatenate value[0][1] in every record.
    rows.sort()  # Sort the list alphabetically.
    for row in rows:
        fname = row[0]
        lname = row[1]
        full_name = fname + " " + lname
        print(full_name)


def companies_users_jobs():  # get jobs from the clients.
    order = []
    for row in rows:
        order.append(row[7])
    order.sort()
    print(order)


open_csv("../files/testFile.csv")
earliest_check_in_date()
last_check_in_date()
customer_full_names()
companies_users_jobs()
