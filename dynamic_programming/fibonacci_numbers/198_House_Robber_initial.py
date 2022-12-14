class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        bruteforce [TLE]
        """
        res = [float('-inf')]
        def permutate(curSum, curArr):
            if not curArr:
                res[0] = max(curSum, res[0])
                return
            for i,val in enumerate(curArr):
                permutate(curSum + val, curArr[i+2:])

        permutate(0, nums)

        return res[0]