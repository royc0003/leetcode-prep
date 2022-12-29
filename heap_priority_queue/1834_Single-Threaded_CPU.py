class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        nlogn solution
        '''
        min_heap = []
        process_tasks = []
        # modify the structure so that it's process_time, index, enqueTime
        for i, task in enumerate(tasks):
            eTime, pTime = task[0], task[1]
            process_tasks.append([pTime, i, eTime]) # processTime, index, enqueTime
        # sort by enqueTime
        process_tasks.sort(key = lambda x: x[2])
        # initialize first enqueTime
        cur_time = process_tasks[0][2]
        res = []
        i = 0 
        while i < len(process_tasks) or min_heap:
            # if heap is empty, and cur_time is less than the next elapsed time, update cur_time
            if not min_heap and cur_time < process_tasks[i][2]:
                cur_time = process_tasks[i][2]
            # look ahead; check if enqueTime <= cur_time to be eligible for next task
            while i < len(process_tasks) and process_tasks[i][2] <= cur_time:
                heapq.heappush(min_heap, process_tasks[i])
                i += 1 
            cur_task = heapq.heappop(min_heap)
            cur_time += cur_task[0] # process time
            res.append(cur_task[1]) # append the index
        return res       