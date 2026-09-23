"""
Problem: Q0.37 - Basic_Level_0_Conditional_Statements_6
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-23
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

num = int(input())
if num%400==0 or num%4==0 and num%100!=0:
    print("Leap Year")    
else:
    print("Not a Leap Year")
