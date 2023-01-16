"""
Q6. Write a function that reads in a CSV file and returns a list of dictionaries, where each dictionary
represents a row in the CSV file with the keys being the column names and the values being the cell values.


Example

Input: CSV file containing the following data:
       id,name,age
       1,Alice,20
       2,Bob,25
       3,Charlie,30
Output: [{'id': '1', 'name': 'Alice', 'age': '20'},
         {'id': '2', 'name': 'Bob', 'age': '25'},
         {'id': '3', 'name': 'Charlie', 'age': '30'}]
"""

import csv

# constants
CSV_FILE_PATH = "../assets/employee.csv"


# function to read CSV into dictionary
def translate_csv(csv_file):
    # empty list to hold the final results
    result = []
    # open the CSV file in read mode and get all the rows in dictionary format
    with open(csv_file, 'r') as file:
        rows = csv.DictReader(file)
        for row in rows:
            result.append(row)
    return result


print(translate_csv(CSV_FILE_PATH))
