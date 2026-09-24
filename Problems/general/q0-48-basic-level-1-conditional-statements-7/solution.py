"""
Problem: Q0.48 - Basic_Level_1_Conditional_Statements_7
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-24
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1 , char , num2 = input().split()
num1 = int(num1)
num2 = int(num2)
if char== '+':
    print(num1+num2)
elif char == '-':
    print(num1 - num2)
elif char == '*':
    print(num1 * num2)
else:
    print(num1/num2)
