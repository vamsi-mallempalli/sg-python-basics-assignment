"""
Q3. Write a generator function that yields the next prime number on each iteration.

Sample Input output

Input: 5
Output: [2, 3, 5, 7, 11]

Input: 10
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
"""


# function to check if the given nunber is a prime or not
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# generator to return one prime number each time it's called
def prime_numbers_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


# function to use generator and return first n prime numbers
def get_first_n_prime_numbers(n):
    prime_numbers = []
    prime_gen = prime_numbers_generator()
    for i in range(n):
        prime_numbers.append(next(prime_gen))
    return prime_numbers


exit_flag = 'N'
while exit_flag.upper() != 'Y':
    try:
        number_of_primes = int(input("Number of prime numbers to print:"))
        print(get_first_n_prime_numbers(number_of_primes))
        exit_flag = input("Do you want to exit(y=exit): ")
    except ValueError as verr:
        print("Invalid input. Please try again")



