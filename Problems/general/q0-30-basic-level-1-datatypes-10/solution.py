"""
Problem: Q0.30 - Basic_level_1_Datatypes_10
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-22
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
num1 , num2 , num3 , num4 = map(int,input().split())
x = num1 if num1<num2 else num2
y = num2 if num1<num2 else num1

z = num3 if num3<num4 else num4
w = num4 if num3<num4 else num3

p = x if x<z else z
q = z if x<z else x

r = y if y<w else w
s = w if y<w else y
print(p,q if q < r else r, r if q<r else q,s)
