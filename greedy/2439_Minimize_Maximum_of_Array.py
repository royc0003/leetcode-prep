class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        '''
        [3,7,1,6]
        [0,3,10,11,17] -- prefix sum approach
        3 / 1 --> 3
        10 / 2 --> 5
        11 // 3 --> 4
        17 // 4 -> 5
        '''
        prefix_sum = 0
        res = float('-inf')
        for i, num in enumerate(nums):
            prefix_sum += num
            res = max(res, math.ceil(prefix_sum / (i+1)))
        
        return res