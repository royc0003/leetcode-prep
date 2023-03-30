class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])

        # top-down approach, to handle repeated cases
        cache = {}
        def dfs(r,c, prev_val):
            # check if cur_val > prev_val
            if r < 0 or r == ROW or c < 0 or c == COL or matrix[r][c] <= prev_val:
                return 0
            # cache values that have been seen
            if (r,c) in cache:
                return cache[(r,c)]

            cur_val = matrix[r][c]
            left = 1 + dfs(r, c-1, cur_val)
            right = 1 + dfs(r, c+1, cur_val)
            down = 1 + dfs(r+1, c, cur_val)
            up = 1 + dfs(r-1, c , cur_val)
            cache[(r,c)] =max(left, right, down, up)
            return cache[(r,c)]
        res = float('-inf')
        for r in range(ROW):
            for c in range(COL):
                potential_res = dfs(r,c,-1)
                res = max(res, potential_res)
        return res
