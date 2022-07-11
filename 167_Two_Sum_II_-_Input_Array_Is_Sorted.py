class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Since this is a sorted array, we should consider using 2-pointers opp. direction pattern.
        
        if sum of 2  > target, we move right -= 1
        if sum of 2 < target, we move left += 1
        '''
        l, r = 0, len(numbers)-1
        
        while l < r:
            sum_of_two = numbers[l] + numbers[r]
            if sum_of_two == target:
                return [l+1, r+1]
            elif sum_of_two > target:
                r -=1
            else:
                l += 1
            
        
        