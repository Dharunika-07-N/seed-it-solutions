"""
Problem: Q0.29 - Basic_level_1_Datatypes_9
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-22
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1 , num2 , num3 = map(int,input().split())
maxx = num1 if num1 > num2 and num1 > num3 else num2 if num2>num1 and num2 > num3 else num3
minn = num1 if num1 < num2 and num1 < num3 else num2 if num2<num1 and num2<num3 else num3
mid = num1 + num2 + num3 - minn - maxx
space = " "
print(minn," ",mid," ",maxx)
