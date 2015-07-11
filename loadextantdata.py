__author__ = 'David'

import csv

def get_data():
    """
    This will get data from the csv downloaded from google and feed it to the database
    as valid information.
    :return:
    """
    data = []
    with open("Oregon Subsidized and Affordable Housing_3-6-2013.csv") as csv_file:
        all_data = csv.reader(csv_file)
        row = 0
        for line in all_data:
            row += 1
            sub_data = []
            col = 0
            for item in line:
                col += 1
                try:
                    sub_data.append(item)
                except UnicodeDecodeError:
                    print("Non Utf-8 character in csv at row {} col {}".format(row, col))
            data.append(sub_data)
        return data

get_data()
