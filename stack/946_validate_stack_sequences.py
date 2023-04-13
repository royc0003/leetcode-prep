class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        [1]
        [1,2,3,4,5] ---
                 ^
        [4,5,3,2,1]

        stack = []
        [1,2,3,4,5]
                 ^
        [1,2,3,4,5]
----------------------------
        
        [1,2]

        [1,2,3,4,5]
                 ^
        [4,3,5,1,2]  
               ^
        '''
        l, r = 0, 0 
        stack = []
        while l < len(pushed) and r < len(popped):
            stack.append(pushed[l])
            l += 1
            while stack and stack[-1] == popped[r]:
                stack.pop()
                r += 1
        return len(stack) == 0
            
