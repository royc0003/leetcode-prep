class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        PROBLEM about this solution: O(M*N)^2 -- exceeded execution time
        
        1. For each grid, we run a bfs. 
        2. As we do a BFS if we hit the gate, then update the global val
        3. End of BFS, we will update the current grid
        """
        ROW, COL = len(rooms), len(rooms[0])
        
        def bfs(i, j, rooms, ROW, COL):
            # Initialize queue | visited set
            queue, visited = deque(), set()
            
            # Initilaize overall count
            res = 2147483647
            
            # mark as visited
            visited.add((i,j))
            # add ot queue
            queue.append((i,j, 0))
            
            allDirections = [(0,1), (0,-1), (-1,0), (1,0)]
            
            # while q is not empty
            while queue:
                
                i, j, length = queue.popleft()
                
                # if we hit a gate, we update to the min
                if rooms[i][j] == 0:
                    res = min(res, length)
                    
                
                for direction in allDirections:
                    neighbRow, neighbCol = direction[0] + i, direction[1] + j
                    
                    # check within boundaries
                    if ROW > neighbRow >= 0 and COL > neighbCol >= 0 and rooms[neighbRow][neighbCol] != -1:
                        # check if not visited and within boundaries
                        if (neighbRow, neighbCol) not in visited:
                            # add to q
                            queue.append((neighbRow, neighbCol, length+1))
                            # add to visited
                            visited.add((neighbRow, neighbCol))
            return res
                    
            
            # for each adj, check if not visited and within boundaries
                # mark as visited
                # and add to queue
        
        for i in range(ROW):
            for j in range(COL):
                if rooms[i][j] == 2147483647:
                    res = bfs(i, j, rooms, ROW, COL)
                    rooms[i][j] = res
                
        
        