class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res, curSum = [],  [0]
        curSelection = [] 
        seen = set()
        
        def backtracking(candidates):
            if curSum[0] == target:
                if tuple(curSelection[0::]) in seen:
                    return
                res.append(curSelection[0::]) #deep-copy
                seen.add(tuple(curSelection[0::]))
                return
            if curSum[0] > target:
                return
            
            for i, candidate in enumerate(candidates):
                # select
                curSelection.append(candidate)
                curSum[0] += candidate
                # backtrack
                backtracking(candidates[i+1::])
                # de-select
                curSelection.pop()
                curSum[0] -= candidate
        
        backtracking(candidates)
        return res
        
        