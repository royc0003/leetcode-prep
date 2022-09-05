class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        1. check if the newInterval's end is < the curInterval's start.
        2. if newInterval's start is > curInterval's start, we append current interval
        3. there is an overlap where newInterval's end is >= start and newInterval's start <= end. then we change the newInterval value
        4. handle edge case by appending the newInterval at the end
        '''
        mergedList = [] 
        
        for i, interval in enumerate(intervals):
            newStart, newEnd = newInterval
            if newEnd < interval[0]:
                mergedList.append(newInterval)
                return mergedList + intervals[i::] 
            # start is greater than the new interval
            elif newStart > interval[1]:
                mergedList.append(interval)
            else: # we have a overlapping interval
                newInterval = [min(newStart, interval[0]), max(newEnd, interval[1])]
                
        mergedList.append(newInterval) # why?
        return mergedList
            
        