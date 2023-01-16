"""
Q7. Write a function that takes a list of numbers and returns the sum of the numbers that are divisible by 3 or 5.
The function should use a generator expression to accomplish this.


Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 33

Input: [0, 15, 30, 45, 60, 75, 90, 105]
Output: 330
"""


# lambda function to get the sum of 3/5 divisibles
sum_of_3_or_5_divisibles = lambda input_numbers: sum((i for i in input_numbers if i % 3 == 0 or i % 5 == 0))


# try out the lambda function
print(sum_of_3_or_5_divisibles([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_of_3_or_5_divisibles([0, 15, 30, 45, 60, 75, 90, 105]))

# try against user inputs
while True:
    try:
        list_of_numbers = list(map(int, input("Enter list of integers separated by space: ").split()))
        break
    except ValueError:
        print("Invalid input. Please enter valid integers.")

print(sum_of_3_or_5_divisibles(list_of_numbers))
