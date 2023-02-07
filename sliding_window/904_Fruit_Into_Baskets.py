class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        Complexity: O(N) time; O(N) space
        Idea:
        - sliding window Solution
        - From left to right, continuously pick and count
        - If the total_type exceeds > 2, we need to reduce the window

        {
            0: 0
            1: 1
            2: 2
        }
        '''
        fruit_mapping = {}
        l = 0
        max_res = float('-inf')
        for r, type_of_fruit in enumerate(fruits):
            fruit_mapping[type_of_fruit] = fruit_mapping.get(type_of_fruit, 0) + 1
            while l < r and len(fruit_mapping) > 2:
                fruit_mapping[fruits[l]] -= 1
                if fruit_mapping[fruits[l]] == 0:
                    del fruit_mapping[fruits[l]]
                l += 1
            max_res = max(r-l+1, max_res)
        return max_res if max_res != float('-inf') else 0 