class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        '''
        use path signature
        complexity: O(M*N)
        '''
        ROW, COL = len(grid), len(grid[0])
        res = set()
        def dfs(r, c, cur_path):
            if r < 0 or r == ROW or c < 0 or c == COL or grid[r][c] != 1:
                return
            # mark as visited
            grid[r][c] = -1
            resultant_path.append(cur_path)
            dfs(r+1, c, "d")
            dfs(r-1, c, "u")
            dfs(r, c+1, "r")
            dfs(r, c-1, "l")
            # take note of edge-case:: record backtracking due to similar encoding
            resultant_path.append('0')

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    resultant_path = []
                    dfs(r,c, "")
                    if resultant_path:
                        res.add(''.join(resultant_path))
        return len(res)