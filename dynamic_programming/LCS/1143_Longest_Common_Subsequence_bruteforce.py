class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Time Complexity: O(2^(n+m))
        Space Complexity: O(N+M)
        '''

        def bruteforce(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            
            # if both char matches, move on to next index for both strings
            if text1[i1] == text2[i2]:
                return 1 + bruteforce(i1+1, i2+1)
            # if don't match we move the index of the each strings independently
            sub_string1 = bruteforce(i1+1, i2)
            sub_string2 = bruteforce(i1+1, i2)
            return max(sub_string1, sub_string2)
        
        res = bruteforce(0,0)
        return res