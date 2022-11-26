class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        (1) have 2 sorted arrays: start and end meetings
        (2) if start < end; we know a single meeting room must occur; so total meeting +1
        (3) if start >= end; we know  we can decrement the meeting room count, because a meeting has ended
        
        sample test:
        [0, 10, 20]
        [10, 12, 30]
        count = 1; 2 
        start: 0.  ----- 10
                         10--12.  
                                20----30
        totalRoom needed is 1. 
        
        '''
        startMeet, endMeet = [], [] 
        res = 0 
        for start, end in intervals:
            startMeet.append(start)
            endMeet.append(end)
            
        # nlogn solution
        startMeet.sort()
        endMeet.sort()
        
        i, j = 0, 0 
        countMeet = 0 
        while i < len(startMeet) and j < len(endMeet):
            minVal = min(startMeet[i], endMeet[j])
            # check if the minval is startMeet
            if minVal == startMeet[i] and startMeet[i] < endMeet[j]:
                countMeet += 1
                i += 1
                res = max(res, countMeet)
                continue
            countMeet -=1 
            j += 1
        
        return res
            
                
        
        
        
        