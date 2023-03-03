class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        top-down solution
        '''
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        ROW, COL = len(dp), len(dp[0])

        # initialize row with 1 -> len(word2)
        for i in range(1, len(word2)+1):
            dp[0][i] = i
        # handle initial column with 1 -> len(word1)
        for i in range(1, len(word1)+1):
            dp[i][0] = i
        
        for i in range(1, ROW):
            for j in range(1, COL):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        return dp[ROW-1][COL-1]