class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        '''
        1. Sort 
        2. Create the prfix arr
        3. Perform a right bounded binary search
        '''
        # sort
        nums.sort()
        # prefix arr
        prefix = 0
        ans = [0] * (len(nums)+1)
        for i in range(1,len(ans)):
            prefix += nums[i-1]
            ans[i] = prefix
        def right_bounded_binary_search(target):
            # [left, mid) [mid + 1, right)
            l, r = 0, len(ans)
            while l < r:
                mid = (l+r) // 2
                if ans[mid] == target:
                    l = mid + 1
                elif ans[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l - 1
        res = []
        for query in queries:
            res.append(right_bounded_binary_search(query))
        return res





