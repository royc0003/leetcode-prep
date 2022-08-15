class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        Solution:
        - iterate backwards
        - if the previous value is larger than current char,
        perform a minus operation
        - else perform a '+' operation
        
        '''
        symbolMap = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        
        res, prev_val = 0, -1 
        
        # traverse backwards
        i = len(s) - 1     
        while i >= 0:
            # check if prev val us larger than cur val
            cur_val = symbolMap[s[i]]
            if cur_val < prev_val:
                res -= cur_val
            else:
                res += cur_val
            # update prev_val
            prev_val = symbolMap[s[i]]
            i -= 1
        return res
                
            
            
            
            
            
            
            
        
        
        
        
        