class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        O(1) space solution
        '''
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0 
        
        for interval in intervals[1::]:
            curStart, curEnd = interval
            # no overlap
            if curStart >= prevEnd:
                prevEnd = curEnd
            else:
                # there's an onverlap
                res += 1
                prevEnd = min(curEnd, prevEnd)
        return res
            
        