class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Step 1: Build a DAC(Directed Acyclic Graph)
        Step 2: Run a topological sort, making sure that no cycle is found   
        
        0 --> 1 --> 2 --> 3
        '''
        graph = defaultdict(list)
        
        # Build the graph
        for postCourse, preCourse in prerequisites:
            graph[preCourse].append(postCourse)
        
        # Run a topological sort while checking for any cycle formed
        visited, seen = set(), set()
        
        def dfs(courseNo):
            if courseNo in seen:
                return False
            if courseNo in visited:
                return True
            res = False
            
            # include into visited set
            visited.add(courseNo)
            # add into seen cycle set
            seen.add(courseNo)
            for neighbCourse in graph[courseNo]:
                res = dfs(neighbCourse)
                if not res:
                    return False
            # no longer part of the path
            seen.remove(courseNo)
            return True
        
        for course in range(0, numCourses+1):
            if not dfs(course):
                return False
        return True
                
        
        
        
        