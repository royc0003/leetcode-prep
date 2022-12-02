class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        Reference: abbccc {a:1, b:2, c:3} 
        
        Cur_word:  aabccc {a:2, b:1, c:3}
        
        look for matching count, for every matching perform a swap and see if they match
        '''
        # handle edge case
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False
        
        ref_count_map, cur_count_map = {}, {}
        
        i = 0 
        while i < len(word1):
            word_1_char = word1[i]
            word_2_char = word2[i]
            cur_count_map[word_1_char] = cur_count_map.get(word_1_char,0) + 1
            ref_count_map[word_2_char] = ref_count_map.get(word_2_char, 0) + 1
            i += 1
        
        ref_arr, cur_arr = [], [] 
        
        for key, count in ref_count_map.items():
            ref_arr.append(count)
        for key, count in cur_count_map.items():
            cur_arr.append(count)
        
        ref_arr.sort()
        cur_arr.sort()
        
        if ref_arr == cur_arr:
            return True
        return False
        
        
        
        
        
        
        