class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        dp[i] = DP[i + len(matched_string)]
        O(N^3), first `N` for iterating through String S, second `N` for iterating through wordDict
        , and third `N` for substring and string matching complexity
        '''
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i+len(word)) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                    if dp[i]:
                        break
        return dp[0]