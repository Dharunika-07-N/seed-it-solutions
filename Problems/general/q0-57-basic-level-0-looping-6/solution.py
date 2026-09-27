"""
Problem: Q0.57 - Basic_Level_0_Looping_6
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-27
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
n = int(input())
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")
