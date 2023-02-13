class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        Top-Down Memoization Approach
        O(N)
        '''
        cache = {}
        def decode(i, cache):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0 
            if i == len(s) - 1:
                return 1
            if i in cache:
                return cache[i]
            one_digit = decode(i+1, cache)
            two_digits = 0 
            if int(s[i:i+2]) <= 26:
                two_digits = decode(i+2, cache)
            cache[i] = one_digit + two_digits
            return cache[i]
        return decode(0, cache)