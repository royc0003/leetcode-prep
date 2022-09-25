class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        L, R = 0, len(matrix[0]) - 1
        
        while L < R:
            for i in range(R - L):
                top, bottom = L, R
                topLeft = matrix[top][L+i]
                # move bototm-left to top-left
                matrix[top][L+i] = matrix[bottom-i][L]
                # move bottom right to bottom left
                matrix[bottom-i][L] = matrix[bottom][R-i]
                # move top right to bottom right
                matrix[bottom][R-i] = matrix[top+i][R]
                matrix[top+i][R] = topLeft
            L += 1
            R -= 1
            
                
                
                