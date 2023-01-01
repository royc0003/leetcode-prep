class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {} # <"a" : 'dog'> <cur_pattern : cur_word>
        s_arr = s.split(" ")
        if len(s_arr) != len(pattern):
            return False
        if len(set(pattern)) != len(set(s_arr)):
            return False
        for i in range(len(pattern)):
            cur_word = s_arr[i]
            cur_pattern = pattern[i] 
            if cur_pattern not in pattern_map:
                pattern_map[cur_pattern] = cur_word
            elif pattern_map[cur_pattern] != cur_word:
                return False
        return True