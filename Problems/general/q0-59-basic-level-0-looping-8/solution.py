"""
Problem: Q0.59 - Basic_Level_0_Looping_8
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-27
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1 = int(input())
ans = "NO"
for i in range(num1):
    if 2**i == num1:
        ans = "YES"
print(ans)
