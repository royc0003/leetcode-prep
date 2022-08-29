class KthLargest:
    '''
    the trick to this is, think from bottom to top.
    e.g. if i want 3rd element from left, ans = 3. 
    [1,2,3,4]
    however, essentially, we can always maintain the array such that the length of the array == k.
    and return the final element. e.g. [1,2,3]
    overall time complexity:
    constuctor + m-times of `add`:
    O(lgN + M*lgN)
    '''

    def __init__(self, k: int, nums: List[int]):# Constructor's time complexity: O(N + N*lgN) => O(lgN)
        self.minHeap, self.k = nums, k 
        heapq.heapify(self.minHeap) # O(N)
        while len(self.minHeap) > self.k: # O(N-k * lgN); and if k == 1, we can reduce to O(N*lgN)
            heapq.heappop(self.minHeap) 
        

    def add(self, val: int) -> int:       # M times of add(); O(M*lgN)
        heapq.heappush(self.minHeap, val) # O(lgN)
        if len(self.minHeap) > self.k:    # O(lgN)
            heapq.heappop(self.minHeap)
        return self.minHeap[0] # return the smallest element, which is also essentially, the 3rd element.
        
    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)