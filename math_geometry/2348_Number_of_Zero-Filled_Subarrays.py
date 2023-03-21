class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        '''
        O(N) solution
        '''
        potential, res = 0, 0 
        for num in nums:
            if num == 0:
                res += (potential) + 1
                potential += 1
            else:
                # reset potential if not valid
                potential = 0
        return res