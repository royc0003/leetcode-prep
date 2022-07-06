class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
         topological sort:
            Each node, v, is visited only after all it dependencies have been visited.
            And then just reverse.
            
        Step 1: Build the directed graph (or adj list)
        Step 2: Run a dfs making sure that:
                - check for cycle -> if there's cycle, return []
                - after visiting depencies, include into results
        Step 3: make sure to reverse the results. results[::-1]
        '''
        # Step 1: Build the graph
        course_map = defaultdict(list)
        for courses in prerequisites:
            course_b, course_a = courses[0], courses[1]
            course_map[course_a].append(course_b)
        
        # Step 2: run the dfs
        visited, cycle = set(), set()
        res = []
        
        def dfs(course):
            # Base case
            if course in cycle:
                return False
            if course in visited:
                return True
            # include into cycle
            cycle.add(course)
            
            for neighb_course in course_map[course]:
                if dfs(neighb_course) == False:
                    return False
            
            # remove from cycle
            cycle.remove(course)
            # include into visited
            visited.add(course)
            # append the results, because all depencies have been visited
            res.append(course)
            return True
        
        for course_no in range(numCourses):
            if not dfs(course_no):
                return []
        return res[::-1]
            
        