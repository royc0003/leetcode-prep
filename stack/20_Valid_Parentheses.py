class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. hashMap < Key = close paran, val = open paran >
        2. check if open paranthesis, and push into stack
        3. check if close paranthesis -> (1) stack is not empty and (2) matching corresponding open paranthesis
        4. stack pop
        O(N) time and O(N) space
        '''
        
        hashMap = { ')': '(', '}' : '{', ']': '[' }
        stack = [] 
        
        for c in s:
            if c not in hashMap: 
                stack.append(c) # open paran
                continue
            elif not stack or stack[-1] != hashMap[c]: # does not match with corresponding open paran
                return False
            stack.pop()
        
        return not stack # check if there's any remaining paran left in stack
        