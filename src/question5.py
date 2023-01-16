"""Q5. Write a function or lambda function (preferably) that takes a list of strings and returns
a new list with all strings sorted in descending order of length.

Input: ["dog", "cat", "bird"]
Output: ['bird', 'cat', 'dog']

Input: ["python", "java", "c++"]
Output: ["python", "java", "c++"]
"""


# lambda function to sort strings by length
sort_by_len_desc = lambda s: sorted(s, key=len, reverse=True)

# try out the lambda function
print(sort_by_len_desc(["dog", "cat", "bird"]))
print(sort_by_len_desc(["python",  "c++", "java"]))
print(sort_by_len_desc(["aa", "BBBB", "ccc", "CCC"]))