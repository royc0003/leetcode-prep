class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        Use top-down memoization approach
        O(N^2)
        '''
        cache = {}
        ROW, COL = len(matrix), len(matrix[0])
        minSum = [float('inf')]

        def dfs(r,c):
            if r < 0 or r == ROW or c < 0 or c == COL:
                return float('inf') 
            if (r,c) in cache:
                return cache[(r,c)]
            # base case to check for the minSum seen thus far
            if r == ROW-1:
                return matrix[r][c]

            middle = dfs(r+ 1, c)
            left = dfs(r + 1, c - 1)
            right = dfs(r + 1, c + 1)

            cache[(r,c)] = min(left, min(middle,right)) + matrix[r][c]
            return cache[(r,c)]

        # Iterate from the top
        for r in range(0,1):
            for c in range(COL):                # O(N)
                res = dfs(r,c)                  # O(N)
                minSum[0] = min(minSum[0], res) # Therefore, O(N^2)

        return int(minSum[0])