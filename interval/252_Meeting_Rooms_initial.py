class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        '''
        greedy:
        only save the prevEnd
        similar to the `non_overlapping`
        '''
        if not intervals:
            return True
        intervals.sort()
        prevEnd = intervals[0][1]
        
        for interval in intervals[1:]:
            curStart, curEnd = interval
            if curStart < prevEnd:
                return False
            prevEnd = curEnd
        return True
        