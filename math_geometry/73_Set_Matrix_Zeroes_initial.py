class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        
        0,0  0,1  0,2
        1,0  1,1  1,2
        2,0, 2,1  2,2
        
        1    2.   3.    4
        5.   0.   7.    8
        0    10.  11.   12
        13.   14. 15.   0 
        """
        queue = deque()
        ROW, COL = len(matrix), len(matrix[0])
        
        # collect all that are == '0'
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    queue.append((r,c))
                    
        
        while queue:
            curRow, curCol = queue.popleft()
            # row
            for c in range(COL):
                if (curRow,c) == (curRow, curCol):
                    continue
                matrix[curRow][c] = 0
            # col
            for r in range(ROW):
                if (r, curCol) == (curRow, curCol):
                    continue
                matrix[r][curCol] = 0
                
            
                
        
        