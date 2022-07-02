"""
Code by Peter Solis
CSE 111 Section 20
Instructor - William Clements
Assignment: W11 Teach - Pupils Sort
"""

import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    # read pupil file to a list
    pupil_list = read_compound_list('CSE 111\W11\pupils.csv')

    # lambda to extract student birthdate
    birth_key = lambda pupil: pupil[BIRTHDATE_INDEX]

    # sort using lambda key
    sorted_pupils = sorted(pupil_list, key = birth_key)

    # print sorted list
    print_list(sorted_pupils)

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(list):
    """Take the input list and print each item
    on a separate line.

    Parameter
        list: the list to print.
    """
    for item in list:
        print(item)

    pass

# call main if file is run locally
if __name__ == "__main__":
    main()
