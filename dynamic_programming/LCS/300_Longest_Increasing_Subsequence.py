class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Intuiton: Start iteratively from the back; for each current_item, 
        # check if current_item is < previous_item, then proceed to 
        # perform max(current_item, previous_item+1)
        O(N^2)
        '''
        LCS = [1 for _ in range(0, len(nums))]

        # start from 2nd from last because the last will definitely be a 1
        for i in range(len(nums)-2, -1, -1):
            # check with every previous item
            for j in range(i+1, len(nums)):
                # if current is < previous
                if nums[i] < nums[j]:
                    LCS[i] = max(LCS[i], LCS[j]+1)
        return max(LCS)