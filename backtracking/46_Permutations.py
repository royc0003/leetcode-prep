class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Included `used`.
        backtracking problem.
        
        Just make sure to select something and reduce selectionList
        2 ways to reduce selectionList:
        (1) Splicing
        (2) or just keep track that the number isn't already seen or in the path
        backtrack(path, selectionList)
        remove the selection which you've previously completed
        '''
        res, seen = [], []
        used = [False] * len(nums)
        
        def permutate(seen,nums):
            if seen and len(seen) == len(nums):
                res.append(seen[0::])
                return
            
            for i in range(len(nums)):
                # prevent from re-running the same item twice
                if used[i]: # this is O(N) we can make it better by using a set
                    continue
                # update `used`
                used[i] = True
                # make a selection
                seen.append(nums[i])
                # backtrack
                permutate(seen, nums)
                # remove from selection
                seen.pop()
                # update `used`
                used[i] = False
        
        permutate(seen, nums)
                
        return res
                
            
            
        