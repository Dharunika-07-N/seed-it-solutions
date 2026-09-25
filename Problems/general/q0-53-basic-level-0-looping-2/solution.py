"""
Problem: Q0.53 - Basic_Level_0_Looping_2
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-25
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1 ,num2 = map(int,input().split())
for i in range(num1,num2+1):
    print(i,end=" ")
