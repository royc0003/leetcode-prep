class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        '''
        postfix
        [2,5,3,9,5,3]
        [0, 2, 7, 10, 19, 24, 27]               #(preifx, index)
        [27,25,20,17,  8,  3,  0]                #(postfix_item, index)
        '''
        prefix_arr, postfix_arr = [0]*(len(nums)+1), [0]*(len(nums)+1)
        
        # prefix_arr_cal
        cur_prefix_sum = 0 
        for i, num in enumerate(nums):
            prefix_arr[i] = [cur_prefix_sum, i]
            cur_prefix_sum += num
        prefix_arr[len(prefix_arr)-1] = [cur_prefix_sum, len(prefix_arr)-1]
        
        cur_postifx_sum = 0 
        for i in range(len(postfix_arr)-1, -1, -1):
            cur_num = nums[i-1] 
            postfix_arr[i] = [cur_postifx_sum, len(postfix_arr)-i-1]
            cur_postifx_sum += cur_num
        
        # greedy method
        minRes = [float('inf'), None] # sum, index
        
        i = 1
        while i < len(prefix_arr):
            pre_res = prefix_arr[i][0] // prefix_arr[i][1]
            post_res = postfix_arr[i][0] // postfix_arr[i][1] if postfix_arr[i][1] != 0 else 0
            avgRes = abs(pre_res - post_res)
            print(avgRes)
            curMinRes = minRes[0]
            if avgRes < curMinRes:
                minRes = [avgRes, i]
            i += 1
        return minRes[1] - 1
        
        
        
        
        
        