class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        bucket sort algo
        
        '''
        # Step 1: Create bucket list
        bucket = [[] for _ in range(len(nums)+1)]
        
        # Step 2: freqMap
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        # Step3 : transfer into bucket
        for num, freq in freqMap.items():
            bucket[freq].append(num)
        
        # Step 4: flatten list
        flattened_list = []
        
        for i in range(len(bucket)-1, -1, -1):
            if k  <= 0:
                break
            if bucket[i]:
                for item in bucket[i]:
                    if k <= 0:
                        break
                    flattened_list.append(item)
                    k -= 1
        
        return flattened_list
        
        
        