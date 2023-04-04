class Solution:
    def partitionString(self, s: str) -> int:
        '''
        abacaba
        ^ ^.^ 
        observed_set = (a, c)
        '''
        seen = set()
        l = 0 
        res = 0
        for r in range(len(s)):
            # check valid window
            if s[r] in seen:
                res += 1
                l = r
                seen = set()
            seen.add(s[r])
        res += 1 if l < len(s) else 0
        return res 