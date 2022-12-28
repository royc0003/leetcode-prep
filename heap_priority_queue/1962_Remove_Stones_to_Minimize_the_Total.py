import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        '''
        Intuition: 
        - Apply maximing heap
        - perform ceil using math fn()
        Complexity:
        Time - O(NlgN)
        Space - O(N)
        '''
        # maximizing heap operation
        # min heap by default
        max_heap = [-1 * pile for pile in piles]
        # apply heapify
        heapq.heapify(max_heap)

        count = k 
        while count > 0:
            # pop
            cur_max_pile = -1 * heapq.heappop(max_heap)
            # apply floor division
            floored_max_pile = math.ceil(cur_max_pile/2)
            # push back into the maximimzing heap
            heapq.heappush(max_heap, -1 * floored_max_pile)
            count -= 1
        # tabulate results
        res = [ -1 * pile for pile in max_heap]
        return sum(res)