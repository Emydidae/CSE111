"""
Code by Peter Solis
CSE 111 Section 20
Instructor - William Clements
Assignment: W09 Team - Students
"""

import csv

def main():
    # create dictionary of student IDs
    path = 'CSE 111\W9\students.csv'
    student_dict = read_dict(path)
    # query user and give response
    user_id = input('Please enter an I-Number (xxxxxxxxx): ')
    if user_id in student_dict:
        print(student_dict[user_id])
    else:
        print('No such student.')

def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    temp_dict = {}
    # open file
    with open(filename, 'rt') as text_file:
        # make file into object
        csv_obj = csv.reader(text_file)
        # ask if there's a header
        header_q = input('Is there a header row in the data? (Answer Y or N)\n')
        if header_q == 'y' or header_q == 'Y':
            next(csv_obj)
        # bring into dictionary
        for row in csv_obj:
            key = row[0]
            temp_dict[key] = row[1]
    return temp_dict

if __name__ == "__main__":
    main()