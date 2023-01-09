class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROW, COL = m, n
        # create the initial table 
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]
        # fill the initial row
        for r in range(ROW):
            dp[r][0] = 1
        # fill the first col w 1's
        for c in range(COL):
            dp[0][c] = 1
        for r in range(1, ROW):
            for c in range(1, COL):
                # current_grid = look top + look left
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[ROW-1][COL-1]