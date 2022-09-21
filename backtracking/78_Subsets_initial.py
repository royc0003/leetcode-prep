class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 
        curSelection = [] 
        
        def backtrack(nums):
            res.append(curSelection[0::])
            for i, selection in enumerate(nums):
                # select
                curSelection.append(selection)
                # backtrack
                backtrack(nums[i+1:])
                # de-select
                curSelection.pop()
        backtrack(nums)
        return res
        
        