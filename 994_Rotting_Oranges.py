class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Notice: Instead of using set(), we used variable
        Start with initializing variables of fresh_oranges and queue
        Start by iterating through; for every rotten orange, we add to queue, for every fresh orange, we += 1
        RUN BFS Simultaneously, remembering to update orange to rotten,  and appending to the queue. 
        Return final results only if fresh oranges == 0, else -1 
        '''
        
        time_elapsed = 0
        ROW, COL = len(grid), len(grid[0])
        queue, fresh_oranges = deque(), [0]
        
        # Search for rotten oranges and add into queue
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh_oranges[0] += 1
        
        
        def bfs(i,j):
            # check for boundary & not fresh orange
            if i == ROW or i < 0 or j == COL or j < 0 or grid[i][j] != 1:
                return
            
            # add to queue
            queue.append((i,j))
            # mark curent gird to 2 to indicate as rotten
            grid[i][j] = 2
            # remove from fresh_oranges
            fresh_oranges[0] -= 1
            
        
        while queue and fresh_oranges[0] > 0:
            cur_len = len(queue)
            for _ in range(cur_len):
                i,j = queue.popleft()
                bfs(i+1, j)
                bfs(i-1, j)
                bfs(i, j+1)
                bfs(i, j-1)
            # increment after succesful elapsed
            time_elapsed += 1
                
                
        return time_elapsed if fresh_oranges[0] == 0  else -1
                
                    
        