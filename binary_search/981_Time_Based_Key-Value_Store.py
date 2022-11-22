class TimeMap:
    
    def __init__(self):
        self.keyValMap = defaultdict(list) # {key: <val, time>}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        Note: this is already sorted value;
        because time series is in increasing order
        '''
        self.keyValMap[key].append([value, timestamp])

            

    def get(self, key: str, timestamp: int) -> str:
        # binary search
        cur_array = self.keyValMap[key]
        
        l, r = 0, len(cur_array) - 1
        closestItem = ""
        # optimal solution
        while l <= r:
            mid = (l+r) // 2
            if cur_array[mid][1] == timestamp:
                return cur_array[mid][0]
            # 2 , 1(given)
            elif timestamp >= cur_array[mid][1]:
                closestItem = cur_array[mid]
                l = mid + 1
            else:
                r = mid - 1
        return closestItem[0] if closestItem != "" else closestItem
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)