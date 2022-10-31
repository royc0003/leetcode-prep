class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Step 1: find all the rotten items
        Step 2: BFS to rot everything
        Step 3: anything that reminas will be what we ant
        """
        
        ROW, COL = len(board), len(board[0])
        queue = deque()
        # Pass 1: Save a set of items that violate the board rules
        for r in range(ROW):
            for c in range(COL):
                if r == 0 or r == ROW -1 or c == 0 or c == COL -1:
                    queue.append((r,c))
                    
        # Pass 2: Perform rotting on all the adjacent values
        while queue:
            r,c = queue.popleft()
            # out of bound
            if r < 0 or r == ROW or c < 0 or c == COL or board[r][c] != "O":
                continue
            board[r][c] = "."
            queue.append((r+1,c))
            queue.append((r-1,c))
            queue.append((r,c+1))
            queue.append((r,c-1))
        
        # Pass 3: we flip everyhting else base on the rules provided
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == '.':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
    
            
                
            
        