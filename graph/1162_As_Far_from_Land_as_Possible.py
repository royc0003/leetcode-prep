class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        
        def bfs(r, c):
            if r < 0 or r == ROW or c < 0 or c == COL or grid[r][c] == 1:
                return
            grid[r][c] = 1
            queue.append((r,c))
        
        total_possible_area, total_land, total_water = 0, 0 ,0 
        queue = collections.deque()
        for r in range(0, ROW):
            for c in range(0, COL):
                total_possible_area += 1
                if grid[r][c] == 1:
                    queue.append((r,c))
                    total_land += 1
                if grid[r][c] == 0:
                    total_water += 1
        if total_possible_area == total_land or total_possible_area == total_water:
            return -1

        max_distance = -1
        while queue:
            len_q = len(queue)
            for _ in range(0, len_q):
                x = queue.popleft()
                cur_r, cur_c = x[0], x[1]
                bfs(cur_r+1, cur_c)
                bfs(cur_r-1, cur_c)
                bfs(cur_r, cur_c+1)
                bfs(cur_r, cur_c-1)
            max_distance += 1
            
        return max_distance
