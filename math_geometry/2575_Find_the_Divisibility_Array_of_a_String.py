class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        '''
        O(N) solution
        Note: total %= m handles overflow edgecase
        '''
        total = 0
        res = [0] * len(word)
        # try slding window solution
        for i in range(0, len(word)):
            total *= 10
            diff = ord(word[i]) - ord('0')
            total += diff
            total %= m # ATTENTION: handle overflow problem
            if total == 0:
                res[i] = 1
        return res