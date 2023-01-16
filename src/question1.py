"""Write a program,
 Reads in all the lines of the file (take any random or article from wikipedia),
 Create a dictionary, where the key is the line number and value is another dictionary.
 This another dictionary should contain length of the words as keys, and the number of words having same length as values.

Example, first line in the file: "The quick brown fox jumps over the lazy dog"

    output - {
    1: {
    3: 4  # This is comment for explaination. There are four words having 3 chars - the, fox, the, dog
    5: 3  # This is comment for explaination. There are 3 words having 5 chars - quick, brown, jumps
    4: 2  # This is comment for explaination. There are 2 words having 4 chars - over, lazy
    }
}"""
import os

# constants
DEFAULT_FILE_PATH = '../assets/ipl_info.txt'


def count_word_length(file_path):
    # Dictionary to store the final result
    lines = {}

    # Open the file in read mode and read all the lines
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file):
            word_length_count = {}
            # for each line count the word lengths
            for word in line.split():
                # if length already exists, then increment the count
                if len(word) in word_length_count:
                    word_length_count[len(word)] += 1
                else:
                    word_length_count[len(word)] = 1
            lines[line_num + 1] = word_length_count

    return lines


# get the file path from user - Eg: ..\assets\ipl_info.txt
file_path = input("Please enter file path:")

# if file does not exist, default to the sample file
if not os.path.exists(file_path):
    print(f'{file_path} does not exist. Defaulted to sample file {DEFAULT_FILE_PATH}.')

# call word count function
print(count_word_length(DEFAULT_FILE_PATH))