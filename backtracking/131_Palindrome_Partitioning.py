class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        O(N*2^N); where first `N` refers to palindrome checking and 2^N, 2^N Choices
        '''
        res, part = [], []
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(i):
            if i >= len(s):
                res.append(part[:]) #deep-copy
                return 
            for r in range(i, len(s)):
                if is_palindrome(i, r):
                    part.append(s[i:r+1])
                    dfs(r+1)
                    part.pop()
        dfs(0)
        return res