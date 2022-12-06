import pandas as pd
import math
import heapq

df = pd.read_csv('day_1.csv', skip_blank_lines=False)
arr = []
for item in df['data']:
    if math.isnan(item):
        arr.append(' ')
    else:
        arr.append(int(item))

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

def part_2_heapify():
    df = pd.read_csv('day_1.csv', skip_blank_lines=False)
    arr = []
    for item in df['data']:
        if math.isnan(item):
            arr.append(' ')
        else:
            arr.append(int(item))

    maxSum = float('-inf')
    # heap
    maxHeap = []
    l = 0 
    curSum = 0 
    for r, val in enumerate(arr):
        curSum += val if val != ' ' else 0 
        if (r + 1) < len(arr) and arr[r+1] == ' ':
            maxSum = max(curSum, maxSum)
            maxHeap.append(-1 * curSum) # maxHeap (-ve); default: minHeap
            curSum = 0 
            l = r + 2 if (r + 2) < len(arr) else None
    heapq.heapify(maxHeap) # O(N); create the heap
    i = 0 
    res = 0
    while i < 3:
        cur_max_item_from_heap = -1 * heapq.heappop(maxHeap)
        res += cur_max_item_from_heap
        i += 1
    print(res)
part_2_bucket_sort()
