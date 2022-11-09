class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        
        0/1 KnapSack problem
        O(2^N)
        '''
        res = set()
        
        def dfs(curString, leftParanLen, rightParanLen):
            if leftParanLen == n and rightParanLen == n:
                # make a copy of curString
                tempRes = curString
                res.add(tempRes) if tempRes not in res else None
                return
            if leftParanLen > n or rightParanLen > n:
                return
            
            
            # choose not add 
            if rightParanLen < leftParanLen:
                dfs(curString + ')', leftParanLen, rightParanLen + 1)
            # choose to add
            dfs(curString + '(', leftParanLen + 1, rightParanLen)
        
        dfs('', 0 ,0)
        return res
            
            
        
        
        
        
        