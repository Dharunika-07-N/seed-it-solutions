"""
Problem: Q0.55 - Basic_Level_0_Looping_4
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-25
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num = int(input())
ans = 1
for i in range(1,num+1):
    ans *= i
print(ans)
