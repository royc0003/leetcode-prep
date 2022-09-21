class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        +ve-diagonal = row + col
        -ve-diagonal = row - col
        1. baseCase is when row == ROW - 1 
        2. backtrack():
            - check if the current selection is valid by checking against the COL set(), +ve-diag Set(), -ve-diag Set()
            - if valid we make a selection
            - backtrack(row + 1)
            - remove selection
        '''
        ROW, COL = n, n 
        colMap, posDiagMap, negDiagMap = set(), set(), set()
        res = []
        board = [["."] * n for i in range(n)]

        
        def checkValid(col, pos, neg):
            if col in colMap or pos in posDiagMap or neg in negDiagMap:
                return False
            return True
        
        
        def backtrack(row):
            if row == ROW :
                tmpRes = []
                for boardRow in board:
                    tmpRes.append("".join(boardRow[0::])) #deep-copy
                res.append(tmpRes)
            
            for col in range(COL):
                pos = row + col
                neg = row - col 
                if not checkValid(col, pos, neg):
                    continue
                # make a selection
                board[row][col] = 'Q'
                # add to the colMap
                colMap.add(col)
                # add to posMap
                posDiagMap.add(pos)
                # add to negMap
                negDiagMap.add(neg)
                # backtrack
                backtrack(row + 1)
                # deselect
                board[row][col] = '.'
                colMap.remove(col)
                posDiagMap.remove(pos)
                negDiagMap.remove(neg)
                
        # boardCreation()
        backtrack(0)
        return res
            
                
                
                
                
                
                
        
        