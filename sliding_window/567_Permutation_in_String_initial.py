class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Complexity: O(N * 2^N)
        '''
        # look for the shorter one
        A, B = s1, s2
        if len(s2) < len(s1):
            A, B = s2, s1  # Where A is the short, and B is the long one
        # the length of the string will determine the size of the window
        def permutate(path, s):
            '''
                      []
                    /
                []
            '''
            if len(path) == len(s1):
                if ''.join(path) == s1:
                    return True
                return False
            res = False
            # select a path
            for letter in s:
                path.append(letter)
                res = permutate(path, s)
                if res:
                    return True
                path.pop()
            return False
            
            
        l = 0 
        freqMap = {} 
        lenA = len(A)
        for r, val in enumerate(B):
            # include into freqMap
            freqMap[val] = freqMap.get(val,0) + 1
            if (r - l + 1 == lenA):
                # check i fboth strings are the same
                if permutate([], s2[l:r+1]):
                    return True
                freqMap[s2[l]] -= 1
                l += 1
                
        return False
            
        
        
        