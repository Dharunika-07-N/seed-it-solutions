"""
Problem: Q0.40 - Basic_Level_0_Conditional_Statements_9
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-23
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

num = int(input())
dictt = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
ans = " "
for x , y in dictt.items():
    if num == x:
        ans = y
        break
    else:
        ans = "Invalid"
        
print(ans)
