"""
Problem: Q0.49 - Basic_Level_1_Conditional_Statements_8
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-24
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
x , y = map(int,input().split())
if x == 0 and y == 0:
    print("Point lies at the origin")
elif x>0 and y >0:
    print("Point lies in the First quandrant")
elif x<0 and y>0:
    print("Point lies in the Second quandrant")
elif x<0 and y<0:
    print("Point lies in the Third quandrant")
elif x>0 and y<0:
    print("Point lies in the Fourth quandrant")
