"""
Problem: Q0.39 - Basic_Level_0_Conditional_Statements_8
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-23
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

num = int(input())
dictt = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
ans = " "
for x , y in dictt.items():
    if num == x:
        ans = y
        break
    else:
        ans = "Invalid"
        
print(ans)
