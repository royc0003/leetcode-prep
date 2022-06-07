class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        1. Define the boundaries
        2. Make sure to declare visited, in-place.
        mark as -1 for visited
        
        ROW = 3 
        
        i < ROW and i >= 0 
        i < 0 or i >= ROW
        ROW <= i < 0 
        '''
        ROW, COL = len(grid), len(grid[0])
        
        globalCounter = 0 
        
        def dfs(i, j, grid):
            # Boundary check or Base Case
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] == '0' or grid[i][j] == '-1':
                return
            
            # mark as visited
            grid[i][j] = '-1'
            
            allDirections = [(0,1), (0,-1), (1,0), (-1,0)]
            
            # Get directions
            for direction in allDirections:
                neighbRow, neighbCol = direction[0] + i, direction[1] + j
                dfs(neighbRow, neighbCol, grid)
        
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    dfs(i,j, grid)
                    # every successful dfs, we increment the global counter
                    globalCounter += 1
        
        return globalCounter
    
