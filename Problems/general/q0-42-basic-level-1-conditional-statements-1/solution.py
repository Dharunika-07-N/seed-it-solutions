"""
Problem: Q0.42 - Basic_Level_1_Conditional_Statements_1
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-24
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
marks = int(input())
Grade = ' '
if marks>=91:
    Grade = 'A'
elif marks >=76 and marks<=90:
    Grade = 'B'
elif marks >=61 and marks<=75:
    Grade = 'C'
else:
    Grade = 'D'

print(f"Grade {Grade}")
