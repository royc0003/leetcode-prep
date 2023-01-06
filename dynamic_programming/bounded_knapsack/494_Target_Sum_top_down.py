class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity: O(N*M)
        '''
            
        cache = {}
        def topDown(i, cur_sum):
            if i == len(nums) and cur_sum != target:
                return 0
            if i == len(nums) and cur_sum == target:
                return 1
            if (i, cur_sum) in cache:
                return cache[(i, cur_sum)]

            positive = topDown(i+1, cur_sum+nums[i])
            negative = topDown(i+1, cur_sum - nums[i])
            cache[(i, cur_sum)] = positive + negative
            return cache[(i, cur_sum)]
        return topDown(0,0)