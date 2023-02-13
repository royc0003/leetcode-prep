class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        min_so_far, max_so_far = 1, 1

        for i, num in enumerate(nums):
            if num == 0:
                min_so_far, max_so_far = 1, 1
                continue
            tmp = min_so_far
            min_so_far = min(min_so_far * num, max_so_far * num, num)
            max_so_far = max(tmp * num, max_so_far * num, num)
            res = max(res, max_so_far)
        return res