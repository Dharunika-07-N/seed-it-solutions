"""
Problem: Q0.68 - Basic_Level_1_Looping_7
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-28
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num = int(input())
summ = 0
for i in range(1,num+1):
    if num % i == 0:
        summ+=i
print(summ)
