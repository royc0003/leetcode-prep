class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        O(N) complexity
        '''
        count_map = {}
        res = float('-inf')
        l = 0
        for r, char in enumerate(s):
            count_map[char] = count_map.get(char, 0) + 1

            while len(count_map) > k:
                count_map[s[l]] -= 1
                if count_map[s[l]] == 0:
                    del(count_map[s[l]])
                l += 1
            res = max(res, r-l+1)
        return res
            