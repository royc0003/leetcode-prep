class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Kadane's algorithm 
        '''
        
        # 2 pointers approach
        maxSum, curSum = nums[0], 0
        L = 0
        
        for R in range(len(nums)):
            if curSum < 0: # why care about val < 0??
                curSum = 0 
                L = R
            
            curSum += nums[R]
            maxSum = max(curSum, maxSum)
        return maxSum
        