class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        1. check which interval to begin (new or existing interval)
        2. check if new interval has been inserted, if no, we check if it fits in, otherwise we move on.
        3. Key here is non-overlapping
        [1,2]
        
        [1,3] [2,5] --> 
        
        [1,3], [0,1]
        because 0 < starting 1 
        
        [[0,2], []]
       
        
        '''
        if not intervals:
            return [newInterval]
        
        mergedIntervals = [] 
        
        if newInterval[0] < intervals[0][0]:
            mergedIntervals.append(newInterval)
            newInterval = None
        else:
            mergedIntervals.append(intervals[0])
        
        
        # run through the algo
        for interval in intervals:
            interval_start, interval_end = mergedIntervals[-1]
            cur_start, cur_end = interval
            
            
            # check the new interval first
            if newInterval and newInterval[0] <= interval_end:
                mergedIntervals[-1] = [min(newInterval[0], interval_start), max(interval_end, newInterval[1]) ]
                # clear newInterval
                newInterval = None
                # handle cur start
                if cur_start <= mergedIntervals[-1][1]:
                    mergedIntervals[-1] = [min(cur_start, mergedIntervals[-1][0]), max(cur_end, mergedIntervals[-1][1])]
                else:
                    mergedIntervals.append(interval)
            elif cur_start == interval_start and cur_end ==  interval_end:
                # guard
                continue
            elif cur_start <= interval_end:
                mergedIntervals[-1] = [min(cur_start, interval_start), max(interval_end, cur_end)]
            else:
                mergedIntervals.append(interval)
                
        # check if newIntervals is empty or not
        if newInterval:
            if newInterval[0][1] < 
            mergedIntervals.append(newInterval)
            
        return mergedIntervals 
                
            
        
        
        