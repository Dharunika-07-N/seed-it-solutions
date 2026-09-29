"""
Problem: Q0.70 - Basic_Level_1_Looping_9
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-29
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

# your code goes here
arr = list(map(int,input().split()))
mini = arr[0]
maxx = arr[0]
summ = 0
size = 0
for i in range(len(arr)):
    if arr[i]>0:
        size+=1
        summ+=arr[i]
        if arr[i]< mini:
            mini=arr[i]
        elif arr[i]>maxx:
            maxx = arr[i]
        
    
avg = summ/size
print(f"Min = {mini}")
print(f"Max = {maxx}")
print(f"Sum = {summ}")
print(f"Average = {avg:.6f}")
