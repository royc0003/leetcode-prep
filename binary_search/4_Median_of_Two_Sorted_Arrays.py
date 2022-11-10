class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        1. get the total_len
        2. get the half
        3. and split into 2 partitions (where nums1[0:mid] and nums1[mid+1::])
        
        binary_search will perform the following:
        (1) check if leftPartition_1[mid+1] < leftPartition_2[mid]
        and leftPartition_2[mid+1] < leftPartition_1[mid]
        (2) else, we perform an update on the pointer
        '''
        
        total_len = len(nums1) + len(nums2)
        half = total_len // 2
        # default nums1 to be the shorter one
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1
        
        while True:
            mid_s = (l+r) // 2
            mid_l = half - mid_s - 2 #attention
            
            ALeft = nums1[mid_s] if mid_s >= 0 else float('-infinity')
            ARight = nums1[mid_s+1] if (mid_s + 1) < len(nums1) else float('infinity')
            BLeft = nums2[mid_l] if mid_l >= 0 else float('-infinity')
            BRight = nums2[mid_l+1] if (mid_l+1) < len(nums2) else float('infinity')
            
            if ALeft <= BRight and BLeft <= ARight:
                if total_len % 2 == 1:
                    return min(ARight, BRight)
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            
            elif ALeft > BRight:
                r = mid_s - 1
            else:
                l = mid_s + 1
        
                
            
            
            
        
        
        
        