import pandas as pd
import math

df = pd.read_csv('day_1.csv', skip_blank_lines=False)
arr = []
for item in df['data']:
    if math.isnan(item):
        arr.append(' ')
    else:
        arr.append(int(item))
def part_1():
    maxSum = float('-inf')
    l = 0 
    curSum = 0 
    for r, val in enumerate(arr):
        curSum += val if val != ' ' else 0 
        if (r + 1) < len(arr) and arr[r+1] == ' ':
            maxSum = max(curSum, maxSum)
            curSum = 0 
            l = r + 2 if (r + 2) < len(arr) else None

    print(maxSum)

def part_2():
    pass





