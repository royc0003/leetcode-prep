class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        shows that Floyd's algorithm can be applied to array as well.
        Step 1: Find the initial interesection between fast and slow pointers
        Step 2: Declare the two pointers until they intersect again. The two pointers that intersect
        will be the result 
        '''
        
        slow, fast = 0, 0 
        # Step 1: Find the inital intersection between fast and slow
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # Step 2: Declare two slow pointers until they intersect.
        # The intersection of the two will be the result
        slow2 = 0
        
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow2
            
            
            
        
        