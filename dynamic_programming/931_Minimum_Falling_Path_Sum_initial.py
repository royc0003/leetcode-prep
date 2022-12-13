class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        Initial solution (TLE)
        O(N * 3^N)
        '''
        ROW, COL = len(matrix), len(matrix[0])
        minSum = [float('inf')]
        
        def dfs(r,c, curSum):
            if r < 0 or r == ROW or c < 0 or c == COL:
                return
            # pass the value to next sum
            curSum += matrix[r][c]
            # base case to check for the minSum seen thus far
            if r == ROW-1:
                minSum[0] = min(minSum[0], curSum)
                return
            dfs(r+ 1, c, curSum)
            dfs(r + 1, c - 1, curSum)
            dfs(r + 1, c + 1, curSum)

        # Iterate from the top
        for r in range(0,1):
            for c in range(COL): # O(N)
                dfs(r,c, 0)      # O(3^N)
                                # Therefore, O(N * 3^N)
        return int(minSum[0])

            
            
            
