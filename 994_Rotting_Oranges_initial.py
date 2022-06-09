class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        1. Start with grabbing all the rotten orange
        2. Run the rotting simultaenously (similar to tree BFS)
            Every successfuly run of the tree bfs, we will incremeent the timer
        
        Note: We only traverse the non-empty ones, mark as visited, and put into queue
        '''
        
        time_elapsed = -1
        ROW, COL = len(grid), len(grid[0])
        queue, fresh_oranges = deque(), set()
        
        # Search for rotten oranges and add into queue
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh_oranges.add((i,j))
                    
        # error handling
        if len(fresh_oranges) == 0:
            return 0
        
        def bfs(i,j):
            # check for boundary & not fresh orange
            if i == ROW or i < 0 or j == COL or j < 0 or grid[i][j] != 1:
                return
            
            # add to queue
            queue.append((i,j))
            # mark curent gird to 2 to indicate as rotten
            grid[i][j] = 2
            # remove from fresh_oranges
            fresh_oranges.remove((i,j))
            
        
        while queue:
            cur_len = len(queue)
            for _ in range(cur_len):
                i,j = queue.popleft()
                bfs(i+1, j)
                bfs(i-1, j)
                bfs(i, j+1)
                bfs(i, j-1)
            # increment after succesful elapsed
            time_elapsed += 1
                
                
        return time_elapsed if len(fresh_oranges) == 0 else -1
                
                    
        