"""
Problem: Q0.56 - Basic_Level_0_Looping_5
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-26
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num = int(input())
fac = 1
sum= 0
for i in range(1,num+1):
    fac*=i
    sum+=fac
print(sum)
