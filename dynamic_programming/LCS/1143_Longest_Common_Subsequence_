class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Time Complexity: O(M*N)
        Space Complexity: O(M*N)
        '''
        cache = {}
        def memoization(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            if (i1,i2) in cache:
                return cache[i1,i2]
            
            # if both char matches, move on to next index for both strings
            if text1[i1] == text2[i2]:
                cache[(i1,i2)] = 1 + memoization(i1+1, i2+1)
                return cache[(i1,i2)]
            
            # if don't match, we move the index seperately for both strings
            sub_string1 = memoization(i1+1, i2)
            sub_string2 = memoization(i1, i2+1)
            cache[(i1,i2)] = max(sub_string1, sub_string2)
            return cache[(i1,i2)]
        
        res = memoization(0,0)
        return res