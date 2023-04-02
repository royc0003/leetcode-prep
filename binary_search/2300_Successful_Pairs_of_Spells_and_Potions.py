class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        time-complexity: O(N*logN)
        [1,2,3,4,5]
        cur = 5
        l, r = 0, 5
        3 * 5 = 15 > 7
        r = 2
        mid = 1
        2 * 5 = 10 > 7
        (1) // 2 = 0
        5 * 1 > 7?

        [5, 8 ,8]
        l, r = 0, 3
        8*2 == 16 
        '''
        # left-bounded binary search
        # (l, mid] (mid+1, r]
        def binary_search(multiplier):
            l, r = 0, len(potions)
            while l < r:
                mid = (l+r) // 2
                if (potions[mid] * multiplier) == success:
                    r = mid
                elif (potions[mid] * multiplier) > success:
                    r = mid
                else:
                    l = mid +1
            return len(potions) - l
        
        potions.sort()
        res = []
        for multiplier in spells:
            res.append(binary_search(multiplier))
        return res