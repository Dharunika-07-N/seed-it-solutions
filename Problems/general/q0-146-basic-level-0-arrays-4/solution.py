"""
Problem: Q0.146 - Basic_Level_0_Arrays_4
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
odd_count = 0
even_count = 0
for i in arr:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"Odd = {odd_count}")
print(f"Even = {even_count}")
