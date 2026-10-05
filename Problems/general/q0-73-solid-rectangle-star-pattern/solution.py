"""
Problem: Q0.73 - Solid Rectangle Star Pattern
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-10-05
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

num1,num2 = map(int,input().split());
for i in range(num1):
    print(num2*"*");
