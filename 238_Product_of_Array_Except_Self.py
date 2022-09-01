class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix sum * postfix sum
        O(N)
        '''
        output = [1] * len(nums)
        
        ans = 1 # 2
        for i in range(len(output)):
            output[i] = output[i] * ans
            ans = nums[i] * ans
        
        ans = 1
        for i in range(len(output)-1, -1, -1):
            output[i] = output[i] * ans
            ans = nums[i] * ans
        return output
        
        