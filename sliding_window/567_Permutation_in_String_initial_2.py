class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        O(M * N); where N is used to check across the map
        '''
        # Step 1: count the number of s1
        freqMapS1 = {}
        for i,v in enumerate(s1):
            freqMapS1[v] = freqMapS1.get(v,0) + 1
        
        
        def checkMap(map1, map2):
            for key, val in map1.items():
                if key not in map2:
                    return False
                if key in map2 and map2[key] != val:
                    return False
            return True
        
        freqMapS2 = {} 
        # Run window size
        l = 0 
        for r,v in enumerate(s2):
            freqMapS2[v] = freqMapS2.get(v,0) + 1
            # window size is fit
            if (r - l + 1 == len(s1)):
                if checkMap(freqMapS1, freqMapS2):
                    return True
                freqMapS2[s2[l]] -= 1
                l += 1
                
        return False
            
                
                
            
        
        