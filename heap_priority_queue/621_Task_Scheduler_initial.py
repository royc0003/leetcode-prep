class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        1. create a maxHeap
        2. create a freqMap
        3. create a queue
        
        Steps:
        1. while maxHeap is available, we pop the value, and incremement global time
        2. popped value - 1; and push into global queue with the next available time
        3 if the first value in the queue is available, we push into the maxHeap
        
        
        A A A B B B; n = 2; globalTime = 1
        AB_, 
        012,3 
        queue = [(A,2),(B,3) ]
        freqMap = {
            A : 3
            B : 3
        }
        [3]
        B,2
        
        
        '''
        if n == 0:
            return len(tasks)
        
        maxHeap, freqMap = [], {}
        queue = [] 
        globalTime = 0
        # step 1: count in freqMap
        for c in tasks:
            freqMap[c] = freqMap.get(c, 0) + 1
            
        # Step 2: push into max heap
        for k,v in freqMap.items():
            heapq.heappush(maxHeap, -1 * v)
        
        
        while maxHeap or queue:
            # check if we can push the current queue value into maxHeap
            if queue and queue[0][1] == globalTime:
                heapq.heappush(maxHeap, queue.pop(0)[0])
            # pop value
            curVal = heapq.heappop(maxHeap) if maxHeap else 0 
            # increment global time
            globalTime += 1
            # push to queue only if curVal != 0 
            if curVal == 0 or curVal + 1 == 0:
                continue
            queue.append((curVal + 1, globalTime + n))
            
                
        return globalTime
            
            
        