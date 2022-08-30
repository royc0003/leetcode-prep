class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        O(N) complexity, O(N) Space
        '''
        stack = []
        
        for token in tokens:
            if token == '+' or token == '-' or token == '/' or token == '*':
                res = 0 
                val_x = int(stack.pop())
                val_y = int(stack.pop())
                # opt
                if token == '+':
                    res += (val_y + val_x )
                elif token == '-':
                    res += (val_y - val_x)
                elif token == '/':
                    res = int(val_y / val_x)
                elif token == '*':
                    res = val_y * val_x
                stack.append(res)
            else:
                stack.append(token)   
                
        
        return stack[-1]
                    
                
            
            
            
        