"""
Q8. Write a function that handles the ValueError exception that may be raised when trying to convert a string
to an integer. The function should prompt the user to enter a new string until a valid integer is entered.

Input: '3'
Output: 3

Input: 'abc'
Output: ValueError exception handled, new input prompted.
"""


# function to get user inputs for integer and validate
def read_integer(max_attempts):
    attempts = 0
    # keep trying till maximum attempts reached
    while attempts <= max_attempts:
        try:
            value = input("Please enter an integer: ")
            return f"User input {int(value)}"
        except ValueError as verr:
            print("Exception: ValueError. Please enter valid integer")
        except Exception as err:
            print("Exception: Unknown error. Please enter valid integer")

        attempts += 1
        if attempts == max_attempts:
            return "Reached maximum invalid attempts. Exiting"


# read integer from user
print(read_integer(5))