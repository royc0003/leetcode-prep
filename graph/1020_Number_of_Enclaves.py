class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        Base Case:
        (1) If hit boundary, return False
        (2) If hit `0` return True or is seen 
        '''
        ROW, COL = len(grid), len(grid[0])
        seen = set() 
        def dfs(r,c):
            if r < 0 or r == ROW or c < 0 or c == COL:
                return False
            if (r,c) in seen or grid[r][c] == 0:
                return True
            seen.add((r,c))
            left = dfs(r, c-1)
            right = dfs(r, c+1)
            top = dfs(r-1, c)
            bottom = dfs(r+1, c)
            _tmp = left and right and top and bottom
            if not _tmp:
                return False
            res[0] += 1
            return _tmp
        count = 0 
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in seen and grid[r][c] == 1:
                    res = [0]
                    if not dfs(r,c):
                        continue
                    count += res[0]
        return count
