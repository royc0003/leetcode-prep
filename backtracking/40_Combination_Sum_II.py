class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res, curSum = [],  [0]
        curSelection = [] 
        
        def backtracking(candidates):
            if curSum[0] == target:
                res.append(curSelection[0::]) #deep-copy
                return
            if curSum[0] > target:
                return
            
            prev = -1 
            for i, candidate in enumerate(candidates):
                # prevent from multiple duplicates
                if candidate == prev:
                    continue
                # select
                curSelection.append(candidate)
                curSum[0] += candidate
                # backtrack
                backtracking(candidates[i+1::])
                # de-select
                curSelection.pop()
                curSum[0] -= candidate
                prev = candidate
        
        backtracking(candidates)
        return res
        
        