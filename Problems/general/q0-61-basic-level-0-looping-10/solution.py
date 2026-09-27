"""
Problem: Q0.61 - Basic_Level_0_Looping_10
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-27
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1 , num2 = map(int,input().split())
lcm = 0
for i in range(1,num2+1):
    multiples = num1*i
    if multiples%num2 == 0:
        lcm = multiples
        break
print(lcm)
