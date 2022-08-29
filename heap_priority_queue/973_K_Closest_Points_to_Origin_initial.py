class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        1. put into a list [(euclidean_distance, x, y )]
        2. heapify
        3. pop the values where K > 0 
        
        
        '''
        tmpRes = [ (x**2 + y**2, x, y) for x, y in points ]
        heapq.heapify(tmpRes)
        res = []
        while k > 0:
            vals = heapq.heappop(tmpRes)
            res.append([vals[1],vals[2]])
            k -= 1
        return res
            
        
        