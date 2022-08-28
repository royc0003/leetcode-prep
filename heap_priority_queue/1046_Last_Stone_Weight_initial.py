class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Note: heaviest two stones are done.
        we use maximizing heap, note in python, minimizing heap is the default
        implementaiton
        
        '''
        # Step 1: create the heap
        maxHeap = [-1 * x for x in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            val1 = -1 * heapq.heappop(maxHeap)
            val2 = -1 * heapq.heappop(maxHeap) if maxHeap else 0
            # check conditions
            if val1 == val2:
                continue
            res = abs(val1 - val2)
            heapq.heappush(maxHeap, -1 * res)
        
        # since we will only have one value at the end 
        return -1 * heapq.heappop(maxHeap) if maxHeap else 0
            
            
            
        
        
        
        