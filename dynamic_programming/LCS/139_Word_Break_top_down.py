class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        i, j = 0, 0 # i = s pointer
        cache = {}
        def check_word(i):
            if i >= len(s):
                return True
            if (i) in cache:
                return cache[i]

            accept = False
            cache[i] = accept
            for j, dict_word in enumerate(wordDict):
                if (i+len(dict_word)-1) < len(s) and s[i: i+len(dict_word)] == dict_word:
                    cache[i] = check_word(i+len(wordDict[j]))
                    if cache[i]:
                        break
            return cache[i]
        return check_word(0)