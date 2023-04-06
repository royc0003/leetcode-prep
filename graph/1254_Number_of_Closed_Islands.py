class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
            How to handle ensure hitting boundary?
            Base Case:
            - If hits `1` return True
            - If hits boundary return False
            Time - Complexity: O(M * N), since each grid will be taversed at least once
        '''
        ROW, COL = len(grid), len(grid[0])
        seen = set()
        def dfs(r,c):
            if r < 0 or r == ROW or c < 0 or c == COL:
                return False
            if grid[r][c] == 1 or (r,c) in seen:
                return True
            seen.add((r,c))
            left = dfs(r,c -1)
            right = dfs(r,c +1)
            top = dfs(r-1, c)
            bottom = dfs(r+1, c)
            return left and right and top and bottom
        res = 0 
        for r in range(0, ROW):
            for c in range(0, COL):
                # handle seen here
                if (r,c) not in seen and grid[r][c] == 0:
                    if dfs(r,c):
                        res += 1
        return res