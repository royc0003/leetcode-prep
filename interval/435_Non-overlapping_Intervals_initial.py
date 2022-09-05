class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        
        [Remove overlapping points with the one that ends last.
        
        '''
        intervals.sort()
        res = 0
        mergedList = [intervals[0]]
        
        for interval in intervals[1::]:
            prev_start, prev_end = mergedList[-1]
            cur_start, cur_end = interval
            
            if cur_start < prev_end:
                # remove the ones that end last
                mergedList[-1] = [cur_start, cur_end] if cur_end < prev_end else [prev_start, prev_end]
                res += 1
            else:
                mergedList.append(interval)
        return res
            
        
        