class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        (1) build a freqMap
        (2) iterate through the string, the first freqMap with the char == 1, we return index
        
        '''
        freqTable, uniqueIndex = {}, -1
        
        for i,c in enumerate(s):
            # increment the hash map
            freqTable[s[i]] = freqTable.get(s[i], 0) + 1
        
        for i,c in enumerate(s):
            if freqTable[s[i]] == 1:
                uniqueIndex = i
                return uniqueIndex
        
        
        return uniqueIndex
            
            
        