class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Expand around center solution
        O(N^2)
        '''
        total_count = 0 

        for i in range(len(s)):
            # handle odd
            l,r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total_count += 1
                l -= 1
                r += 1
            
            # handle even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total_count += 1
                l -= 1
                r += 1
        return total_count