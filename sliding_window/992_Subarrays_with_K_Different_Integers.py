class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        '''
        Refer to this for explanation: https://leetcode.com/problems/subarrays-with-k-different-integers/solutions/235235/c-java-with-picture-prefixed-sliding-window/ 
        Time Complexity : O(N) 
        Space Complexity: O(N)
        '''


        pre_count = 0 # keeps track of all possible permutations
        res = 0 
        count_map = {}
        l = 0
        for r, num in enumerate(nums):
            # counts the frequency
            count_map[num]= count_map.get(num,0) + 1

            # check if there's any violation > K
            if len(count_map) > k:
                del(count_map[nums[l]])
                # update left pointer
                l += 1
                # reset prefix due to violation
                pre_count = 0
            
            # check if > 1: meaning, we have more permutations
            while count_map[nums[l]] > 1:
                pre_count += 1
                count_map[nums[l]] -= 1
                l += 1
            
            # check if succeed
            if len(count_map) == k:
                res += pre_count + 1
        return res
            