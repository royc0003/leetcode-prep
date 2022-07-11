class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        2-pointers opposite end pattern.
        
        If height[l] < height[r], we would assume that moving rightwards will increase the height.
        So we move l += 1
        else r -= 1
        
        '''
        
        max_water = float('-inf')
        l, r = 0, len(height)-1
        
        while l < r:
            potential_max = min(height[l], height[r]) * (r - l)
            
            max_water = max(max_water, potential_max)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_water
        
        