from operator import itemgetter
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        1. put all values into a new list [(position, speed)]                            # O(N)
        2. sort() -- [(10,2), (8,4), (0,1), (5,1), (3,3)] --> [(0,1),  (5,1),  (10,2)]   # O(nlogn)
        3. (target - cur_dst) / speed                           12        7       1      # O(N)
        check if item_before's time < item_after's time; if yes, splice out the value. 
        Remember to iterate from the back

        TLE (Time Limt Exceeded)
        
        '''
        # Step 1: put all values into a list
        mergedList = [] 
        stack = [] 
        for i in range(len(position)):
            mergedList.append((position[i], speed[i]))
        # Step 2: Sorted() 
        mergedList.sort(key=itemgetter(0))
        # Step 3: check if item_before's time < item_after's time; if yes, splice out the value
        # from reverse
        i = len(mergedList) - 1
        while i >= 0: 
            curTime = (target-mergedList[i][0])/mergedList[i][1]
            if i == len(mergedList)-1:
                stack.append(curTime)
                i -= 1
                continue
            if curTime <= stack[-1]:
                mergedList = mergedList[0:i] + mergedList[i+1::]
            else:
                stack.append(curTime)
            i -= 1
        return len(mergedList)
            
            
            
        
        
            
        
        
        