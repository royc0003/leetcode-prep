class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) == len(s):
            if s == t:
                return s
            else:
                return ""
        
        sCount, tCount = {}, {}
        l = 0 
        matches = 0         
        for val in t:
            tCount[val] = tCount.get(val,0) + 1
            
        target = len(t)
        res = [s] #start, end
        l = 0
        for r, v in enumerate(s):
            sCount[v] = sCount.get(v,0) + 1
            
            if v in sCount and v in tCount and sCount[v] == tCount[v]:
                matches += 1
            
            while l <= r and matches == target:
                if (r - l  + 1) < len(s):
                    res = s[l:r+1]
                val = s[l]
                if val in sCount and val in tCount and sCount[val] == tCount[val]:
                    matches -= 1
                sCount[val] -= 1
                l += 1
                
        return res if matches > 0 else ""
                
                    
            
        
        
        
        