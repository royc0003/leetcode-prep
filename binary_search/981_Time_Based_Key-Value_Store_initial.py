class TimeMap:
    
    def __init__(self):
        self.keyValMap = defaultdict(set) 
        self.valTimeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        '''
        self.keyValMap[key].add(value)
        
        # handle if key is in set but val not in set 
        # key is present in keyValMap
        valTimeLen = len(self.valTimeMap[value])
        currentArray = self.valTimeMap[value]

        i = 0 
        while i+1 < valTimeLen:
            # check that val >= arr[i] and and val <= arr[i]
            if value >= currentArray[i] and value <= currentArray[i+1]:
                i += 1
        # set current val
        self.valTimeMap[value] = currentArray[0:i] + [timestamp] + currentArray[i+1:]


    def get(self, key: str, timestamp: int) -> str:
        '''
        binary search
        '''
        if key not in self.keyValMap:
            return ""
        valArray = self.keyValMap[key]
        
        for val in valArray:
            sortedArray = self.valTimeMap[val]
            l, r = 0 , len(sortedArray)-1 
            while l <= r:
                mid = (l + r) // 2
                if sortedArray[mid] == timestamp:
                    return val
                elif timestamp < sortedArray[mid]:
                    r = mid
                else:
                    return val
        return ""
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)