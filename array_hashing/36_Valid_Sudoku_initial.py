class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        3 sets:
        - row_set
        - col_set 
        - key: val(set)
        
        board0:{1,2,3,4,5,}
        
        '''
        rowSet, colSet = defaultdict(set), defaultdict(set)
        boardSet = defaultdict(set)
        
        ROW, COL = len(board), len(board[0])
        # 1st pass create the sets
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] != ".":
                    val = board[r][c]
                    curBoardRow, curBoardCol = r // 3, c // 3
                    if r in rowSet and val in rowSet[r]:
                        return False
                    if c in colSet and val in colSet[c]:
                        return False
                    if (curBoardRow,curBoardCol) in boardSet and val in boardSet[(curBoardRow,curBoardCol)]:
                        return False
                    # check the board's box 
                    rowSet[r].add(val)
                    colSet[c].add(val)
                    boardSet[(curBoardRow, curBoardCol)].add(val)
                      
        return True
        
                
                
        
        