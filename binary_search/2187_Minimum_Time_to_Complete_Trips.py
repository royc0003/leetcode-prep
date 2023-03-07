class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        '''
        0 1 2 3 4 5 6
              - at each time, check if can fulfill totalTrips;
        - left bounded binary search, to find minimum
        O(M*LogN)
        '''
        def check_meet_total_trips(target_time):
            trips_to_reach = totalTrips
            for t in time:
                trips_to_reach -= (target_time // t)
            return trips_to_reach <= 0
        
        l, r = 1, max(time) * totalTrips
        # [L, mid) [mid+1, R)
        while l < r:
            mid = (l+r) // 2
            # if meets, then we need to push to the left boundary
            if check_meet_total_trips(mid):
                r = mid
            else:
                l = mid + 1
        return l
