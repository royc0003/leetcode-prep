class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1. If we are within range where l < r, we are in a sorted array; simply return  replace existing minimum_res = min(minimum_res, nums[l]) which is the smallest val. and break
        2. greedily update the minimum_res with the mid value
        3. If you're on the left portion of the array; search for right portion of the array
        4. If you're on the right porition of the sorted array; search for left portion
        
        '''
        
        l, r = 0, len(nums) - 1
        res = float('inf')
        
        while(l <= r):
            
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            mid = l + (r-l)//2
            res = min(nums[mid], res)
            # left portion of the sorted array
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
                
            
        
                
            
        