class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        '''
        minimizing heap
        time: O(N lgN)
        space: O(N)
        '''
        min_heap = sticks
        # apply heapify O(N) 
        heapq.heapify(min_heap)
        # loop through
        res = 0
        while len(min_heap) > 1:
            x = heapq.heappop(min_heap)
            y = heapq.heappop(min_heap) if min_heap else 0
            cur_res = x + y 
            res += cur_res
            heapq.heappush(min_heap, cur_res)
        return res