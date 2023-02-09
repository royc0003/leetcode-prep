class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        '''
        bfs
        O(M*N)
        '''
        queue = collections.deque()
        ROW, COL = len(grid), len(grid[0])
        def bfs(cur_row, cur_col):
            if cur_row < 0 or cur_row == ROW or cur_col < 0 or cur_col == COL or grid[cur_row][cur_col] == 'X' or grid[cur_row][cur_col] == -1:
                return
            # mark as seen
            grid[cur_row][cur_col] = -1
            queue.append((cur_row, cur_col))
        goal = None
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '*':
                    goal = (r,c)
                if grid[r][c] == '#':
                    queue.append((r,c))
        total_time = 0
        while queue:
            total_len_of_q = len(queue)
            for _ in range(total_len_of_q):
                cur_r, cur_c = queue.popleft()
                # check if goal has been reached
                if (cur_r, cur_c) == goal:
                    return total_time
                bfs(cur_r+1, cur_c)
                bfs(cur_r-1, cur_c)
                bfs(cur_r, cur_c+1)
                bfs(cur_r, cur_c-1)
            total_time += 1
        return -1
