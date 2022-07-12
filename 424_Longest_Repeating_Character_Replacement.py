class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Think of what is the inner valid condition to close
        sizeOfWindow - MostFreqCount = no_of_replacement
        if no_of_replacement <= k; we can continue to proceed with tabulating the size, and the total length
        
        '''
        
        l, count_map = 0 , {}
        max_res = 0
        
        def most_freq_value_from_map():
            return sorted(count_map.values(), reverse = True)[0]
        
        for r, v in enumerate(s):
            # add to frequency map
            count_map[v] = count_map.get(v, 0) + 1
            
            total_replacement = (r-l +1) - most_freq_value_from_map()
            # Step 2: check for valid condition to close the window
            while(total_replacement > k):
                count_map[s[l]] -= 1
                l += 1
                total_replacement -= 1
            
            max_res = max(max_res, r-l + 1)
            
        return max_res
        
        