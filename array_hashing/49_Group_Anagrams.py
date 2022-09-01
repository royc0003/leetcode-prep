class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        
        pefroming sorted()
        the timing would've been, 
        nlogn -- for each sorting of string
        and m -- length of the array
        therefore, m * nlogn
        
        we can reduce the overall complexity to  m * n, without sorting and using count as the key of the map.
        '''
        
        ans = defaultdict(list)
        
        for word in strs:
            count = [0] * 26 # a ... z
            # count the number of characters we have found
            for c in word:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(word)
        return ans.values()
            
        