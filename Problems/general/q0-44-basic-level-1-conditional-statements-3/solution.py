"""
Problem: Q0.44 - Basic_Level_1_Conditional_Statements_3
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-24
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1,num2,num3 = map(int,input().split())
if num1+num2 > num3 and num1+num3 > num2 and num2+num3 > num1:
    print("Valid")
else:
    print("Not Valid")
