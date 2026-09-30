"""
Problem: Q0.147 - Basic_Level_0_Arrays_5
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-30
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
size = int(input())
arr = list(map(int,input().split()))
summ = 0
for i in range(len(arr)):
    print(f"{summ}",end=" ")
    summ+=arr[i]
