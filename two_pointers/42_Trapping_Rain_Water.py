class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Core Concept here is:
        curWater = min(LMAX, RMAX) - curHeight[i]
        (1) brute force method - O(N^2)
        (2) memoization LMAX, RMAX 3 pass - O(N) space 
        (3) 2 pointers approach (optimal with O(1) space)
        '''
        L, R = 0, len(height)-1
        res = 0 
        LMAX, RMAX = height[0], height[len(height)-1]
        
        while L <= R:
            # Update LMAX and RMAX
            LMAX = max (height[L], LMAX)
            RMAX = max (height[R], RMAX)
            
            if LMAX < RMAX:
                res += abs((LMAX - height[L]))
                L += 1 
            else:
                res += abs((RMAX - height[R]))
                R -= 1
        return res
        
        
        
        