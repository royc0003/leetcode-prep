class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        1. Have a visited set or peform an in-place visited
        2. Run a dfs on every island to calculate the max area of it
        '''
        ROW, COL = len(grid), len(grid[0])
        
        def dfs(r,c):
            # check for boundary and check that it's not in visited
            if r == ROW or r < 0 or c == COL or c < 0 or grid[r][c] != 1:
                return 0
            # in-place mark as visited
            grid[r][c] = -1
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))
            
            
        max_result = 0
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_result = max(max_result, dfs(r,c))
        return max_result