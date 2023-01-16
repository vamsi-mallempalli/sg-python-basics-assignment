"""
Q2. Write a decorator that measures the execution time of a function and logs the result to a file.
"""
import time
from datetime import datetime


def log_function_performance(func):
    def wrapper(*args, **kwargs):
        # record start time
        start_time = datetime.now()
        # execute the function
        result = func(*args, **kwargs)
        # record end time
        end_time = datetime.now()
        with open(f"../performance_logs/FUNC_{func.__name__}.txt", "a") as f:
            f.write(f"Function started at {start_time} and ended at {end_time}. It took {end_time - start_time} seconds to "
                    f"complete.\n")
        return result

    return wrapper


@log_function_performance
def count_characters(string, char):
    count = 0
    for s in string:
        if s == char:
            count += 1
    time.sleep(2)  # This line is for testing purpose only
    return count


print("Char count result:", count_characters("Hello World", "l"))
