class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        O(nLgM)
         # curHour > h, eating too little
         # curHour < h, eatting too much
        
        '''
        minPile, maxPile = min(piles), max(piles)
        l,r = 1 , maxPile
        while l < r:
            mid = (r + l) // 2
            curHour = 0
            for pile in piles:
                remainder = 1 if pile % mid != 0 else 0
                val = pile // mid if pile >= mid else 0 
                curHour += val + remainder
            if curHour > h:
                l = mid +1
            else:
                r = mid
        return l
                
            
                
           