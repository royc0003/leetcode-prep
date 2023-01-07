class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(N^2) solution

        length = 0 
        pointers = (0,0)

        for i in range(len(s)):
            # handle odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l +1) > length:
                    length = (r - l +1)
                    pointers = (l,r)
                l -= 1
                r += 1
            
            # handle even length
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = (r-l+1)
                    pointers = (l,r)
                l -= 1
                r += 1

        return s[pointers[0]:pointers[1]+1]