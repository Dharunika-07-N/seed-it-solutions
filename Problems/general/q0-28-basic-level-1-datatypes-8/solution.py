"""
Problem: Q0.28 - Basic_level_1_Datatypes_8
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-22
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1 , num2 , num3 = map(int,input().split())
maxx = num3
maxx = num1 if num1 > num2 and num1 > num3 else num2
print(maxx)
