import collections
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort by first, then second
        intervals = sorted(intervals, key= lambda x: (x[0], x[1]))
        # Stores query_val: index 
        query_index_map = collections.defaultdict(set) # {1: (index_1, index_2, ..., index_n)}
        # because, query will be sorted, need to keep track of original index of each value before sorting
        for i, query in enumerate(queries):
            query_index_map[query].add(i)
        queries.sort()
        min_heap = [] # [distance, end]
        res = [0] * len(queries)
        i = 0 # index of intervals
        for cur_query in queries:
            cur_index = query_index_map[cur_query].pop()
            # for every interval, if cur_query > `start` of interval, keep pushing into heap
            while i < len(intervals) and cur_query >= intervals[i][0]:
                distance = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(min_heap, [distance, intervals[i][1]])
                i += 1
            # for every top of the heap, if the current query > end_interval; pop()
            while min_heap and cur_query > min_heap[0][1]:
                heapq.heappop(min_heap)
            if min_heap:
                res[cur_index] = min_heap[0][0]
            else:
                # if min_heap is empty, 
                res[cur_index] = -1
        return res
        