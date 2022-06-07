class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        Overall Solution's Complexity: O(M * N)
        We can run bfs starting with the gates instead of the empty path
        Then, run BFS on these gates simultaneously
        """
        ROW, COL = len(rooms), len(rooms[0])
        
        queue, visited = deque(), set()
        
        def bfs(i,j):
            '''
            1. Peform essential boundary checks
            2. If pass boundary check, continue to add in queue and mark as visited
            '''
            if i == ROW or i < 0 or j == COL or j < 0 or rooms[i][j] == -1 or (i,j) in visited:
                return
            # add to queue and mark visited if passes boundary checks
            queue.append((i,j))
            visited.add((i,j))
        
        # Start with searching for all gates
        for i in range(ROW):
            for j in range(COL):
                if rooms[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        
        # This val will be used to increment BFS exploration
        total_dist = 0
        # here we will run bfs Simultaneously == Similar to Tree BFS
        
        while queue:
            cur_len = len(queue)
            
            for _ in range(cur_len):
                i, j = queue.popleft()
                # set the current coordinates with the total_dist
                rooms[i][j] = total_dist
                # peform further exploration
                bfs(i+1, j)
                bfs(i-1, j)
                bfs(i, j+1)
                bfs(i, j-1)
            # increment the total_dist
            total_dist += 1
            
        
            
        
        
        
        
        
        