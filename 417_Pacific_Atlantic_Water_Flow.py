class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Find the interesection between flow of pactific ocean and atlantic ocean.
        
        (0,0) (0,1) (0,2) (0,3)
        (1,0)             (1,3)
        (2,0)             (2,3)
        (3,0)             (3,3)
        :
        :
        (n,0)
        
        '''
        ROW, COL = len(heights), len(heights[0])
        
        pacific_res, atlantic_res = set(), set()
        
        def dfs(r,c, prev_height, res_set):
            # neighb_heigh <= cur_height
            # cur_height >= neighb_height
            # cur_height < neighb_height
            if r  == ROW or r < 0 or c == COL or c < 0 or (r,c) in res_set or prev_height > heights[r][c] :
                return 
            # add to the ocean_set
            res_set.add((r,c))
            # run dfs in neighb_cell
            dfs(r+1, c, heights[r][c], res_set)
            dfs(r-1, c, heights[r][c], res_set)
            dfs(r, c+1, heights[r][c], res_set)
            dfs(r, c-1, heights[r][c], res_set)
            
        for c in range(COL):
            dfs(0,c, heights[0][c], pacific_res)
            dfs(ROW-1, c, heights[ROW-1][c], atlantic_res)
        
        for r in range(ROW):
            dfs(r,0, heights[r][0], pacific_res)
            dfs(r, COL-1, heights[r][COL-1], atlantic_res)
            
        # merge results
        merged_res = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pacific_res and (r,c) in atlantic_res:
                    merged_res.append([r,c])

        return merged_res
            