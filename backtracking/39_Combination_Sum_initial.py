class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        curSum, res = [0], [] 
        curSelection = [] 
        
        def backtrack(candidates):
            if curSum[0] == target:
                res.append(curSelection[0:]) # deep-copy
                return 
            if curSum[0] > target:
                return 
            
            for i, candidate in enumerate(candidates):
                # select
                curSum[0] += candidate
                curSelection.append(candidate)
                # backtrack
                backtrack(candidates[i:]) 
                
                # de-select
                curSum[0] -= candidate
                curSelection.pop() 
                
        backtrack(candidates)
        
        return res
                    
                
                    
                
            
            
            
        
        
        