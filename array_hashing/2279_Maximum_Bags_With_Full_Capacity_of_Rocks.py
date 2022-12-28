class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        '''
        1. Get the difference between two res
        2. check if the diff is < additionalRocks before incrementing the res
        Complexity: O(N)
        Space; O(N) 
        '''
        # apply diff array
        diff_arr = [] 
        for i, cur_cap in enumerate(capacity):
            diff_arr.append(cur_cap - rocks[i])
        # sort diff_arr, in ascending order 
        diff_arr.sort()
        res = 0
        # O(N) solution
        for diff in diff_arr:
            if diff <= additionalRocks:
                res += 1
            additionalRocks -= diff
        return res