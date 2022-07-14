class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Implictly Sorted
        (1) Write an inclusive code
        1, 3 , 5
        mid < t:
          l 
        '''
        l, r = 0, len(nums)-1
        
        while (l <= r):
            mid = l + (r-l)//2
            # check if we're in the left section of the array
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                
            elif nums[mid] <= nums[r]:
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
                
        
        