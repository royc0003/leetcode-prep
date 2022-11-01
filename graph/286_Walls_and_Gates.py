class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        
        again tree bfs
        """
        ROW, COL = len(rooms), len(rooms[0])
        queue = deque()
        seen = set()
        
        # store all gates in the queue
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))
        
        def bfs(r,c):
            if r < 0 or r == ROW or c < 0 or c == COL or rooms[r][c] == -1 or (r,c) in seen:
                return
            queue.append((r,c))
            seen.add((r,c))
            
        totalDist = 0   
        while queue:
            lenQ = len(queue)
            for _ in range(0, lenQ):
                r,c = queue.popleft()
                rooms[r][c] = totalDist
                bfs(r+1, c)
                bfs(r-1, c)
                bfs(r,c-1)
                bfs(r,c+1)
            totalDist += 1
        
        