"""
Problem: Q0.64 - Basic_Level_1_Looping_3
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-27
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
x = int(input())
ans = 0
for i in range(1,x+1):
    if i%2==0:
        ans+=i
    
    
print(ans)
