class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        '''
        O(N) solution
        '''
        nums.sort()
        ans = 0
        mid = len(nums) // 2
        r = mid
        for l in range(0, mid): # ATTENTION. (Alternative) Instead of for r in range
            # check if invalid then move up the right pointer
            while r < len(nums) and (nums[l]*2) > nums[r]:
                r += 1
            if r < len(nums) and (nums[l] *2) <= nums[r]:
                ans += 2
                r += 1
        return ans