class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        bucket sort algo
        '''
        freqMap = {}
        for char in s:
            freqMap[char] = freqMap.get(char, 0) + 1
        
        bucketArr = [[] for _ in range(len(s)+1)]
        
        # put into the bucket
        for char, count in freqMap.items():
            bucketArr[count].append(char)
        
        # decreasing order
        res = []
        for i in range(len(s), -1, -1):
            if len(bucketArr[i]) > 0:
                for item in bucketArr[i]:
                    res.append(i*item)
        return ''.join(res)
        
        