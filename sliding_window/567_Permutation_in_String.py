class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Arr, s2Arr = [0] * 26, [0] * 26
        
        # increment the total counts
        for i in range(len(s1)):
            s1Arr[ord(s1[i]) - ord('a')] += 1
            s2Arr[ord(s2[i]) - ord('a')] += 1
        matches = 0 
        # check for any matches
        for i in range(26):
            matches += 1 if s1Arr[i] == s2Arr[i] else 0 
        
        l = 0 
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # increase count for right
            index = ord(s2[r]) - ord('a')
            s2Arr[index] += 1
            # check if match to increase matches
            if s1Arr[index] == s2Arr[index]:
                matches += 1
            # we added too much
            elif s1Arr[index] + 1 == s2Arr[index]:
                matches -= 1
            
            index2 = ord(s2[l]) - ord('a')
            s2Arr[index2] -= 1
            # check if match to increase matches
            if s1Arr[index2] == s2Arr[index2]:
                matches += 1
            # we added too much
            elif s1Arr[index2] - 1 == s2Arr[index2]:
                matches -= 1
            l += 1
            
        return matches == 26
            
                
        
        
        