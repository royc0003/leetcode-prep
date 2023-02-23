class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        (1) sort by end
        (2) store end as a variable
        (3) iterate through, and if end < next_start, then increment 1
        '''
        points.sort(key = lambda x : x[1])
        res = 1
        prev = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > prev:
                prev = points[i][1]
                res += 1

        return res