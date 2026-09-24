"""
Problem: Q0.45 - Basic_Level_1_Conditional_Statements_4
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-24
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
char = input()
if char in ('a','e','i','o','u') or char in ('A','E','I','O','U'):
    print("Vowel")
else:
    print("Consonant")
