class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = {}
        def permutate(cur_i, n, cache):
            if cur_i >= n:
                return 0
            if (cur_i, n) in cache:
                return cache[(cur_i,n)]
            take = nums[cur_i] + permutate(cur_i + 2, n, cache)
            dont_take = permutate(cur_i + 1, n, cache)
            cache[(cur_i,n)] = max(take, dont_take)
            return cache[(cur_i,n)]
        
        # handle 2 different cases
        #  get the max of (House[1] -> House[n] or House[2] -> House[n-1])
        # E.g. [0,1,2,3,4] -- ranges from 0 to 3 and ranges from 1 to  4
        return max(permutate(0, len(nums)-1, cache), permutate(1, len(nums), cache))