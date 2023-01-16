"""
Q4. Write a function that takes a list of strings and returns a new list with all strings that are anagrams of a
palindrome (i.e., a word or phrase that can be rearranged to form a palindrome). If you can use list comprehension
then it will be better.


Sample Input output

Input: ['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']
Output: ['carcare', 'carecar', 'vicic']

Explanation - carecar and carecar are anagrams of a palindrome racecar. vicic is an anagram of palindrome civic.
lehol is anagram of hello, but hello is not a palindrome, hence lehol is not in the output.

"""


# function to check if two words are anagrams or not
def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


# function to check if the string is palindrome or not
def is_palindrome(num):
    return str(num) == str(num)[::-1]


# function to find anagrams of palindrome.
def anagrams_of_palindrome(input_strings):
    return [s for s in input_strings for p in [s for s in input_strings if is_palindrome(s)] if
            is_anagram(s, p) and s != p]


# try out anagrams_of_palindrome function
print(anagrams_of_palindrome(['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']))
