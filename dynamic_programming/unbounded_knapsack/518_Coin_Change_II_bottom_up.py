class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # Create the DP
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        ROW, COL = len(dp), len(dp[0])
        # fill the column on the most left with `1`
        for i in range(ROW):
            dp[i][0] = 1
        
        # true dp occurs here
        for i in range(ROW):
            for total in range(1, COL):
                # skip
                if i > 0:
                    dp[i][total] = dp[i-1][total]
                # don't skip
                if total >= coins[i]:
                    dp[i][total] += dp[i][total-coins[i]]

        return dp[ROW-1][COL-1]