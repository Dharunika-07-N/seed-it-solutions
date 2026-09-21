"""
Problem: Q0.18 - Basic_level_0_Datatypes_18
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-21
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1 , num2 = input().split()
num1 = float(num1)
num2 = int(num2)

print(f"{num1:.{num2}f}")
