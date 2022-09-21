class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        similar to subset I;
        sort()
        just take note to handle duplicate
        '''
        nums.sort()
        res, curSelection = [], []
        
        def backtrack(nums):
            res.append(curSelection[0:]) #deep-copy
            
            prev = -100
            for i, selection in enumerate(nums):
                # handle duplicate
                if prev == selection:
                    continue
                # select
                curSelection.append(selection)
                # backtrack
                backtrack(nums[i+1:])
                # de-select
                curSelection.pop()
                # assign duplicate
                prev = selection
        backtrack(nums)
        return res
                
                
            