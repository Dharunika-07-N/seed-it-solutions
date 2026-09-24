"""
Problem: Q0.46 - Basic_Level_1_Conditional_Statements_5
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-24
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
char = input()
if char.isalpha():
    print("ALPHABET")
elif char.isalnum():
    print("NUMBER")
else:
    print("SPECIAL CHARACTER")
