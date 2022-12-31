class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        '''
        O(3^N) Time Complexity
        O(N) Space Compleixty
        '''
        ROW, COL = len(grid), len(grid[0])

        total_non_obstacles = 0 
        start_row, start_col = 0, 0 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    start_row, start_col = r, c 
                if grid[r][c] == 0:
                    total_non_obstacles += 1
        total_count = [0]
        seen = set()
        def backtracking(r, c, total_non_obstacles):
            if r < 0 or r == ROW or c < 0 or c == COL or grid[r][c] == -1 or (r,c) in seen:
                return
            if grid[r][c] == 2 and total_non_obstacles == 0:
                total_count[0] += 1
                return
            
            if grid[r][c] == 0:
                total_non_obstacles -= 1
            seen.add((r,c))
            backtracking(r+1, c, total_non_obstacles)
            backtracking(r, c+1, total_non_obstacles)
            backtracking(r-1, c, total_non_obstacles)
            backtracking(r, c-1, total_non_obstacles)
            seen.remove((r,c))

        backtracking(start_row, start_col, total_non_obstacles)
        return total_count[0]