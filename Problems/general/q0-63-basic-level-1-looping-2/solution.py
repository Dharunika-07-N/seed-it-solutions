"""
Problem: Q0.63 - Basic_Level_1_Looping_2
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-27
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
x,y = map(int,input().split())
ans = 0
for i in range(1,x+1):
    ans+=y
    
print(ans)
