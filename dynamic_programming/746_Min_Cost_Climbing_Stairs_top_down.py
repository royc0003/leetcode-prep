class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        O(M*N)
        '''
        # memoization
        cache = {} 
        def min_jump(jump, i):
            # base case
            if i >= len(cost):
                return 0
            if (jump, i) in cache:
                return cache[(jump,i)]
            
            # jump 1 
            c1 = cost[i] + min_jump(jump, i+1)
            # jump 2 steps
            c2 = cost[i] + min_jump(jump, i+2)
            cache[(jump,i)] = min(c1,c2)
            return cache[(jump,i)]
        return min(min_jump(0,0), min_jump(0,1))