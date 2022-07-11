class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Note: This is not ideal at all.
        Remember the input is `Sorted!`
        '''
        
        diff_map = {}
        
        for i,v in enumerate(numbers):
            
            if v in diff_map:
                return sorted([i+1, diff_map[v]+1])
            diff_val = target - v
            diff_map[diff_val] = i
        
            
        
        