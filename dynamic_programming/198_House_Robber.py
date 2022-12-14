class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        top-down memoization approach
        O(N) space and complexity
        """
        cache = {} 
        def permutate(cur_i, cur_arr):
            if cur_i >= len(cur_arr):
                return 0 
            if cur_i in cache:
                return cache[cur_i]

            take = cur_arr[cur_i] + permutate(cur_i + 2, cur_arr)
            skip = permutate(cur_i + 1, cur_arr)

            cache[cur_i] =  max(take, skip)
            return cache[cur_i]
        
        return permutate(0, nums)