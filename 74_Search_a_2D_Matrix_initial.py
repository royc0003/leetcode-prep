class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        (1) look for value within range
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
        
        for r in range(ROW):
            # compare with start of the array
            # compare with end of the array
            if target >= matrix[r][0] and target <= matrix[r][COL-1]:
                return binary_search(matrix[r]) # selects the column to run binary search
        return False
                
                
        
        
            
        
        