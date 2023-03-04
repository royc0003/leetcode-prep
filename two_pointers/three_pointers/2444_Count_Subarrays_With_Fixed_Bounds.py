class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        '''
        three pointers: lmin, lmax and boundary
        Intutition: For every successful boundary, calculate the different permutations that fits within the boundary
        Formula: min(lmin, lmax) - boundary # to give the different permutations

        Complexity: O(N) 
        Space: O(1)
        '''
        lmin, lmax, boundary = -1, -1 ,-1
        res = 0 
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                lmin = -1
                lmax = -1
                boundary = i
            else:
                lmin = i if num == minK else lmin
                lmax = i if num == maxK else lmax
                total_possible_subarrays = min(lmin, lmax) - boundary
                res += max(0, total_possible_subarrays)
        return res