class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
                         1
                        / \
        O(M * N)
        '''

        ROW, COL = len(grid), len(grid[0])
        cache = {}
        def dfs(r, c):
            if r < 0 or r == ROW or c < 0 or c == COL:
                return float('inf')
            if r == ROW-1 and c == COL-1:
                return grid[ROW-1][COL-1]
            if (r,c) in cache:
                return cache[(r,c)]
            down = grid[r][c] + dfs(r+1, c)
            right = grid[r][c] + dfs(r, c+1)
            cache[(r,c)] = min(down, right)
            return cache[(r,c)]
        
        return dfs(0,0)
