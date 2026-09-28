"""
Problem: Q0.67 - Basic_Level_1_Looping_6
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-28
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num = int(input())
for i in range(2,10):
    count = 0
    while num%i == 0:
        count+=1
        num = num // i
    if count>0:
        print(f"{i}->{count}")
