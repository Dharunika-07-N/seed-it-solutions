"""
Problem: Q0.75 - Inverted Right Triangle Star Pattern
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-10-06
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

size = int(input());
for i in range(size,0,-1):
    print("*"*i)
