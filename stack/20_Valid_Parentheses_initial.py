class Solution:
    def isValid(self, s: str) -> bool:
        '''
      condition to pass: 
      - stack is empty
      condition to fail:
       when faced with closing paran:
        - check if empty stack
        - check if presence of corresponding open paran
       - at the end of the string, if stack still has has paran
        '''
        stack = []
        for c in s:
            # guard 
            if c == ')' or c == ']' or c == '}':
                # stack is empty
                if not stack:
                    return False
                if c == ')' and stack[-1] == '(' or c == ']' and stack[-1] == '[' or c == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
                return False
                
            elif c == '(' or c == '[' or c == '{':
                stack.append(c)
        
        return True if len(stack) == 0 else False