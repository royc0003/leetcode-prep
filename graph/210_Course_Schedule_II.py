class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Step 1: Build a DAC graph
        Step 2: Perform a topSort with Cyclical Check
        
        '''
        
        graph = defaultdict(list)
        # Build the graph
        for postCourse, preCourse in prerequisites:
            graph[preCourse].append(postCourse)
            
        topSort = []
        visited, seen = set(), set()
        
        def dfs(courseNo):
            if courseNo in seen:
                return False
            if courseNo in visited:
                return True
            
            res = False
            
            visited.add(courseNo)
            # check for cycle
            seen.add(courseNo)
            for neighbCourse in graph[courseNo]:
                res = dfs(neighbCourse)
                if not res:
                    return False
                
            topSort.append(courseNo)
            # breadcrumb
            seen.remove(courseNo)
            return True
        
        for course in range(0, numCourses):
            if not dfs(course):
                return [] 
        
        return topSort[::-1]