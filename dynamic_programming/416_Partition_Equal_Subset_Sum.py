class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        N * M, where N is the number of subsets, 
        and M is the range of possible targets
        '''
        total_sum = sum(nums)
        if total_sum % 2 != 0 :
            return False
        target = sum(nums)//2
        N,M = len(nums)+1, target + 1
        dp = [[False] * M for _ in range(N)]
        dp[0][0] = True
        
        for i in range(1, N):
            for t in range(0, M):
                if t < nums[i - 1]:
                    dp[i][t] = dp[i - 1][t]
                else:
                    dp[i][t] = dp[i-1][t] or dp[i-1][t - nums[i-1]]
        return dp[len(nums)][target]
                
            
        