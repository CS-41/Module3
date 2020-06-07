"""
Program: average_scores.py
Author: Elizabeth Allen
Last date modified: 06/07/2020

The purpose
The input
The output
"""

import unittest

if __name__ == '__main__':
    first_name = input("Enter your first name: ")  # Input first name
    last_name = input("Enter your last name: ")  # Input last name
    user_age = input("Enter your age: ")  # Input age
    score1 = int(input("Enter 1st score: "))  # Input test scores
    score2 = int(input("Enter 2nd score: "))
    score3 = int(input("Enter 3rd score: "))
    score_list = [score1, score2, score3]

    a = int(sum(score_list))
    b = int(len(score_list))
    c = a // b


    def average(c):
        return c


    average_scores = average(c)

    print(f"Name: {last_name},{first_name}; age: {user_age}; average score: {average_scores}")

unittest.main()
