"""
Problem: Q0.31 - Basic_Level_1_Datatypes_11
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-22
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1 , num2 = map(int,input().split())
print(oct(num1)[2:],hex(num2)[2:].upper())
