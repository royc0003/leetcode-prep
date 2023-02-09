class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        djikstra as the answer
        Intuition: In short, find the minimum_path with its maximum possible height
        O(N^2*LogN)
        Example:
        0 -> 1 -> 3
        |         |
        2 -> 1 -> x

        Djikstra's initial path: 0 -> 1 -> 3; but it's rejected due to 3
        Second path: 0 -> 2 -> 1; accepted as 2 < 3
        '''
        ROW, COL = len(grid), len(grid[0])
        min_heap = [[grid[0][0], 0, 0]]  # weight, src_row, src_col
        visited = set()
        visited.add((0,0))
        while min_heap:
            cur_weight, cur_row, cur_col = heapq.heappop(min_heap)
            if cur_row == ROW-1 and cur_col == COL - 1:
                return cur_weight
            # check all 4 directions
            all_directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for direction in all_directions:
                neighb_row, neighb_col = cur_row + direction[0], cur_col + direction[1]
                # check if within boundary and not visited
                if (neighb_row, neighb_col) in visited or neighb_row < 0 or neighb_row == ROW or neighb_col < 0 or neighb_col == COL:
                    continue
                visited.add((neighb_row, cur_col))
                heapq.heappush(min_heap, [max(cur_weight, grid[neighb_row][neighb_col]),neighb_row, neighb_col])
        return -1 
