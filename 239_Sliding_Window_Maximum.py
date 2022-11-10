class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        monotonic queue (make sure it's descending)
        
        '''
        queue = deque() 
        
        def clean_queue(num):
            while queue and queue[-1] < num:
                # pop right
                queue.pop() 
        def left_pop_if_match(num):
            if queue[0] == num:
                queue.popleft()
        
        l = 0 
        res = []
        
        for r, num in enumerate(nums):
            clean_queue(num)
            queue.append(num)
            
            while (r-l+1) == k:
                res.append(queue[0])
                left_pop_if_match(nums[l])
                l += 1
                
        return res
            
                
            
        