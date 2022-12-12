class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Initial Solution: TLE
        '''

        totalCombi = [0]
        def permutate(_sum):
            if _sum > n:
                return
            if _sum == n:
                totalCombi[0] += 1
                return
            
            for i in range(1,3):
                permutate(_sum+i)
        permutate(0)
        return totalCombi[0]
            