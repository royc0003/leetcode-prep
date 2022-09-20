class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROW, COL = n, n
        res, curSelection = [], []
        seen = set()
        
        def checkValid(r,c):
            # check border
            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return False
            
            res = True 
            directions = [(0,1),(0,-1),(-1,0),(1,0), (1,1),(1,-1),(-1,1),(-1,-1)]
            # check Horizontal, Vertical to see if there's any clash
            for direction in directions:
                next_row, next_col = r + direction[0], c + direction[1]
                if (next_row, next_col) in seen:
                    res = False
                    break
                checkValid(next_row, next_col)
            return res
                
        
        def strBuilderHandler(arr):
            for r,c in arr:
                strBuilder = '.' * (c - 0) + 'Q' + '.' * (COL-1 - c)
                res.append(strBuilder)
                
                
        
        def permute(r,c,curSelection):
            # base case
            if len(curSelection) == 4:
                strBuildrHandler(curSelection)
                return
            # initial for loop
            while r < ROW:
                while c < COL:
                    # check valid first
                    if not checkValid(r,c):
                        c += 1
                        continue
                    # make selection
                    curSelection.append((r,c))
                    seen.add((r,c))
                    # permute
                    permute(r,c,curSelection)
                    # de-select
                    curSelection.pop()
                    seen.remove((r,c))
                    # incremenet col
                    c += 1
                r += 1
                
        permute(0,0,curSelection)

        return res