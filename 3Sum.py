class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1. sort the array, so that we can manage repeated values e.g. [-1,-1]
        2. For repeated values, increment the cur_ptr, and skip all the repeated value
        
        ultimately:
        this is a + 2sum - sorted array(b + c), where we can use 2 pointers on opposite ends.
        '''
        
        nums.sort()
        res = []
        
        for i, v in enumerate(nums):
            
            if i > 0 and nums[i-1] == v:
                continue
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                three_sum = v + nums[l] + nums[r]
                
                if three_sum == 0:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                elif three_sum < 0:
                    l += 1
                else:
                    r -=1 
        
        return res
            
        
        
        