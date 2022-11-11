class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        sCount, tCount = {}, {}
        l = 0 
        matches = 0         
        for val in t:
            tCount[val] = tCount.get(val,0) + 1
            
        target = len(t)
        res = [float('inf'), 0, 0] # window size, start, and end
        l = 0
        for r, v in enumerate(s):
            sCount[v] = sCount.get(v,0) + 1
            
            if v in sCount and v in tCount and sCount[v] == tCount[v]:
                matches += 1
            
            while l <= r and matches == target:
                if (r - l  + 1) < res[0]:
                    res = [r-l+1, l, r]
                val = s[l]
                sCount[val] -= 1
                if val in sCount and val in tCount and sCount[val] < tCount[val]:
                    matches -= 1
                
                l += 1
        startIndex, endIndex = res[1], res[2]
        return s[startIndex:endIndex +1] if res[0] != float('inf') else ""
                
                    
            
        
        
        
        