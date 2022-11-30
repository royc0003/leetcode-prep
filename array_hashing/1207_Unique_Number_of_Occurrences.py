class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        '''
        modified bucket sort method
        Time  Complexity: O(N)
        Space Complexity: O(N)
        '''
        
        countMap = {}
        # count total number
        for num in arr:
            countMap[num] = countMap.get(num,0) + 1
        
        # bucket_array
        bucketArr = [[] for _ in range(len(arr) +1)]
        
        # put into bucket
        for key, count in countMap.items():
            if len(bucketArr[count]) > 0:
                return False
            bucketArr[count].append(key)
        
        return True
            