"""
Problem: Q0.36 - Basic_Level_0_Conditional_Statements_5
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-23
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

num = int(input())
if num%3 == 0 and num%5 == 0:
    print("HiHello")
elif num%5 == 0:
    print("Hello")
else:
    print("Hi")
