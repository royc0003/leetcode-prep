class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        base case:
        (1) if both are out of bounds: return True 
        (2) if pattern is out of bound: return False
        
        if both characters are the same or the the pattern is a '.'
        # can decide to pick a '*' i + 1
        # or not to pick a '*' j + 2
        
        if match: then we perform i + 1 and j + 1
        '''
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            # check if there's a match
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            # there's a star
            if (j + 1) < len(p) and p[j+1] == '*':
                # choose to skip
                cache[(i,j)] = (dfs(i,j+2) or (match and dfs(i+1, j)))
                return cache[(i,j)]
            # there's a match
            if match:
                cache[(i,j)] =  dfs(i+1, j+1)
                return cache[(i,j)]
            
            # everything failed
            cache[(i,j)] = False
            return cache[(i,j)]
        
        return dfs(0,0)
    
    
            
            
                
        
        