class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        
        '''
        freq_map, l = {}, 0
        max_count = 0
        
        for r,v in enumerate(s):
            # include the frequency in the map
            freq_map[v] = freq_map.get(v,0)+1
            
            # if current value in map > 1
            # we repeatedly close the left window
            while l < r and freq_map[v] > 1:
                freq_map[s[l]] -= 1
                l += 1
            
            # get the max count
            max_count = max(max_count, r - l + 1)
            # update right pointer
            r += 1

        
        return max_count
        
                
                
            
        
        