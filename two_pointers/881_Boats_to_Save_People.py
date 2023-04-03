class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        [5,4,3,3]   limit = 5
        ^  ^
        - pseudocode: sort (decreasing manner)
        - Left pointer: largest, right pointer: smallest
        - check if < limit?
            - check right pointer if <= difference
            - if yes, move r pointer leftwards
        - if >= limit, we move left pointer

        3 2 2 1
        ^   ^
        '''
        people.sort(reverse=True)
        l, r = 0, len(people)-1
        total_boats_required = 0

        while l <= r:
            if people[l] >= limit:
                total_boats_required += 1
                l += 1
            else:
                diff = limit - people[l]
                if people[r] <= diff:
                    r -= 1
                    l += 1
                    total_boats_required += 1
                else:
                    l += 1
                    total_boats_required += 1
        return total_boats_required