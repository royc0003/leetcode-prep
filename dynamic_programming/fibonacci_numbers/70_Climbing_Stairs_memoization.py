class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Memoization
        '''

        cache = {}
        def permutate(_steps, cache):
            if _steps > n:
                return 0
            
            if _steps == n:
                return 1
            
            if _steps in cache:
                return cache[_steps]
            
            cache[_steps] = permutate(_steps+1, cache) + permutate(_steps+2, cache)
            return cache[_steps]

        return permutate(0, cache)
            