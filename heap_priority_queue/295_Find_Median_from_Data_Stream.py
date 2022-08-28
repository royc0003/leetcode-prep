class MedianFinder:
    '''
    Soln:
    use two heaps, small (MaxHeap) and large (minHeap); and if maxVal of small > minVal of Large we need to move over to the large heap; check if the differenc ein length of small vs large is not > 1, if yes, we need pop and push to either of lesser length heaps.  
    
    test input: 1, 2, 3
    [1], [2]
    
    '''

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minHeap default

    def addNum(self, num: int) -> None:
        # step 1: include into small heap default
        # take note: python heap is to handle only for max heap
        heapq.heappush(self.small, -1 * num)
        
        #Step 2: check if the max of small > min of large, e.g. [1,7] , [3]
        if self.small and self.large and  -1 * self.small[0] > self.large[0]:
            tmpVal = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * tmpVal)
        
        # Step 3: maintain both heaps such that the difference is no greater than 1 
        if len(self.small) - len(self.large) > 1:
            tmpVal = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * tmpVal)
        elif len(self.large) - len(self.small) > 1:
            tmpVal = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * tmpVal)
    

    def findMedian(self) -> float:
        '''
        if odd length, return one of the medians where length is greater
        if even, take (n, n+1) / 2
        '''
        lengthSum = len(self.small) + len(self.large)
        if lengthSum % 2 == 0:
            return  ((-1 *self.small[0]) +  self.large[0]) / 2
        if len(self.small) > len(self.large):
            return -1 *  self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()