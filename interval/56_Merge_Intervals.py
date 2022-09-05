class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        1. Sort(); and initialize the first value in a stack
        2. if the cur_start <= prev_end, we make sure to update the last element in the stack with the min and max
        '''
        intervals.sort()
        mergedList = [intervals[0]]
        
        for interval in intervals[1::]:
            cur_start, cur_end = interval
            prev_start, prev_end = mergedList[-1]
            if cur_start <= prev_end:
                mergedList[-1] = [min(cur_start, prev_start), max(cur_end, prev_end)]
            else:
                mergedList.append(interval)
                
        return mergedList
        
        