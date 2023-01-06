class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity: O(2^N)
        '''

        def bruteForce(i, cur_sum):
            if i == len(nums) and cur_sum != target:
                return 0
            if i == len(nums) and cur_sum == target:
                return 1
            positive = bruteForce(i+1, cur_sum+nums[i])
            negative = bruteForce(i+1, cur_sum - nums[i])
            return positive + negative
        return bruteForce(0,0)