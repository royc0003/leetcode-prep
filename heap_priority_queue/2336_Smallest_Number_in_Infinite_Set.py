class SmallestInfiniteSet:
    
    def __init__(self):
        self.min_heap = [i for i in range(1, 1001)]
        self.val_set = set(self.min_heap)
        

    def popSmallest(self) -> int:
        if self.min_heap:
            val = heapq.heappop(self.min_heap)
            self.val_set.remove(val)
            return val
        return -1
        

    def addBack(self, num: int) -> None:
        if num not in self.val_set:
            heapq.heappush(self.min_heap, num)
            self.val_set.add(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)