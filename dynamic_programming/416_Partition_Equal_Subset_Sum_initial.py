class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        naive soln O(2^N): brute force soln
                    
        '''
        # if odd we can reject
        if sum(nums) % 2 != 0:
            return False
        target =[sum(nums) // 2]
        
        def knapSack(n: int, curSum: int):
            if curSum == target[0]:
                return True
            
            if n == 0 or curSum > target[0]:
                return False
            
            exists = knapSack(n-1, curSum + nums[n-1]) or knapSack(n-1, curSum)
            return exists
        
        return knapSack(len(nums), 0)
            
        
        
        
        