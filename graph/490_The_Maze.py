class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROW, COL = len(maze), len(maze[0])
        seen = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r == ROW or c == COL or maze[r][c] == 1 or (r,c) in seen:
                return False
            if r == destination[0] and c == destination[1]:
                print('hello')
                return True
            seen.add((r,c))
                            # right. #down   # up.   # left
            all_directions = [(0,1), (1,0), (-1,0), (0,-1)]
            res = False
            for direction in all_directions:
                neighb_row, neighb_col = r, c 
                while (neighb_row + direction[0]) >= 0 and (neighb_row + direction[0]) < ROW and (neighb_col+direction[1]) >= 0 and (neighb_col+direction[1]) < COL and maze[neighb_row + direction[0]][neighb_col + direction[1]] == 0:
                    neighb_row += direction[0]
                    neighb_col += direction[1]
                res = dfs(neighb_row, neighb_col)   
                if res:
                    return True      
            return res

        return dfs(start[0], start[1])