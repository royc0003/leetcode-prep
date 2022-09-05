class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        '''
        can do with simple comparison
        '''
        intervals.sort()
        for i in range(1, len(intervals)):
            i1, i2 = intervals[i-1], intervals[i]
            if i2[0] < i1[1]:
                return False
        return True
        