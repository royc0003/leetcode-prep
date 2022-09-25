class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
         1 - > 2 -> 3
         for i in range ( R - L):
            top, bottom = L, R 
         Top += 1
         for i in range (B - T):
        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2
        
        '''
        Left, Right, Top, Bottom = 0, len(matrix[0]) -1, 0, len(matrix) - 1
        res = [] 
        
        while Left <= Right and Top <= Bottom:
            for i in range(Left, Right + 1):
                res.append(matrix[Top][i])
            Top += 1
            for i in range(Top, Bottom+1):
                res.append(matrix[i][Right])
            Right -= 1
            if not (Left <= Right and Top <= Bottom):
                break
            for i in range(Right, Left-1, - 1):
                res.append(matrix[Bottom][i])
            Bottom -= 1
            for i in range(Bottom, Top - 1, -1):
                res.append(matrix[i][Left])
            Left += 1
            
        return res
                
            
        
        