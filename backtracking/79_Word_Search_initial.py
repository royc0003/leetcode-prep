class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        seen = set()
        
        def backtrack(r,c, word):
            if len(word) == 0:
                return True
            
            if r < 0 or r == ROW or c < 0 or c == COL or (r,c) in seen or board[r][c] != word[0]:
                return False
            
            seen.add((r,c))
            
            res = False
            # dfs method
            neighbors = [(0,1), (0,-1), (-1,0), (1,0)]
            for neighbor in neighbors:
                neighbRow, neighbCol = r + neighbor[0], c + neighbor[1]
                res = backtrack(neighbRow, neighbCol, word[1:])
                if res:
                    break
            # de-select
            seen.remove((r,c))
            return res
                
            
        for r in range(0, ROW):
            for c in range(0, COL):
                if board[r][c] == word[0]:
                    res = backtrack(r,c, word)
                    return res if True else None
                
        return False
        
                    
        
        
        