class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        monotonic stack!
         0.  1. 2. 3. 4. 5. 6. 7 
        [73,74,75,71,69,72,76,73]
        stack=[(76,6),(75,2)
        
        O(N)
        '''
        stack = []
        ans = [0] * len(temperatures)
        
        # check from backwards
        for i in range(len(temperatures)-1, -1, -1):
            # check if  stack peek is smaller than current value
            while stack and stack[-1][0] <= temperatures[i]: #maintains the next highest
                stack.pop() #pop until we make sure the peek of stack will always be next tallest
            
            ans[i] = stack[-1][1] - i if stack else 0
            stack.append((temperatures[i], i))
            
        return ans
        