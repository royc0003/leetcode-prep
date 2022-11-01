class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        graph; tree-bfs
        (1) look for all affected oranges first
        (2) Have a total count on all fresh oranges
        (3) perform bfs rotting
        (4) return timeelapsed only if freshOrange == 0; else -1
        '''
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        freshOranges = [0]
        # Step 1: look for all affected oranges
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshOranges[0] += 1
        # this bfs will perform a check
        def bfs(row,col):
            if row < 0 or row == ROW or col < 0 or col == COL or grid[row][col] != 1:
                return
            # perform rot
            grid[row][col] = 2
            # reduce the totalOranges
            freshOranges[0] -= 1
            queue.append((row,col))
        timeElapsed = 0
        while freshOranges[0] > 0 and queue:
            # tree bfs
            queueLen = len(queue)
            for _ in range(0, queueLen):
                row, col = queue.popleft()
                bfs(row+1, col)
                bfs(row-1, col)
                bfs(row,col+1)
                bfs(row,col-1)
            timeElapsed += 1
        return timeElapsed if freshOranges[0] == 0 else -1
                
                
        
        
        