class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Optimized O(lg(m) * lg(n))
        (1) Binary search on the selected range to look for
        (2) peform binary search on selected range
        Notice: `Sorted` is the keyword to binary searching.
        '''
        def binary_search(nums):
            '''
            (1) think of the closure used; both inclusive
            [l,r]
            (2) l <= r   == termination condition: l == right + 1
            
            1,2,3 --> target = 1, mid = 2
            
            '''
            l = 0 
            r = len(nums)-1
            
            while l <= r:
                mid = l + (r-l)//2
                
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            return False
        # Search in the array
        ROW, COL= len(matrix), len(matrix[0])
        
        l, r = 0, ROW - 1
        while l <= r:
            # this is to handle overflow problem
            mid = l + (r-l)//2
            
            if target >= matrix[mid][0] and target <= matrix[mid][COL-1]:
                return binary_search(matrix[mid])
            elif target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][COL-1]:
                l = mid + 1
        return False
        
        
                
        
        
            
        
        