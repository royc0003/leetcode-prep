class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        1. put into a list [(position, speed)]
        2. sort()
        3. maintain a stack, and check if item_before's speed is < item_after's speed, otherwise we push
        into stack
        
        '''
        mergedList = [[p,s] for p,s in zip(position, speed)]
        mergedList.sort(reverse=True)
        stack = [] 
        for p,s in mergedList:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                continue
        return len(stack)
            
            
        
        