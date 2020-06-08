"""
Program: average_scores.py
Author: Elizabeth Allen
Last date modified: 06/07/2020

The purpose of this program is to show the average of three test scores.
The inputs are first name, last name, age, three test scores.
The output shows the first name, last name, age and the average of the test scores.
"""

import unittest


def average():
    score1 = float(input("Enter 1st score: "))  # Input test scores. Float used for partial credit scores.
    score2 = float(input("Enter 2nd score: "))
    score3 = float(input("Enter 3rd score: "))
    score_list = [score1, score2, score3]
    return sum(score_list) / len(score_list)


if __name__ == '__main__':
    first_name = input("Enter your first name: ")  # Input first name
    last_name = input("Enter your last name: ")  # Input last name
    user_age = int(input("Enter your age: "))  # Input age

    average_scores = average()

    # Output formats the average to print only 2 decimal places
    print("Name: {0},{1}; age: {2}; average score: {3:.2f}".format(last_name, first_name, user_age, average_scores))

unittest.main()

# Tests (focused on averages)
# score1    score2   score3     expected output     actual output
#   50        50       50             50.00             50
#  24.5     60.25     75.75           53.50             53.50
#  100        97        72            89.67             89.67
#   9         10        8.5           9.17              9.17
#   75      84.50     94.25           84.58             84.58
