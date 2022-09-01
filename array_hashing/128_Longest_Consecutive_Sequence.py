class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        check if the number is at the start of the sequence befor eiterating
        '''
        setOfNums = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in setOfNums:
                count = num
                while count + 1 in setOfNums:
                    count += 1
                longest = max(longest, count - num + 1)
        
        return longest
        