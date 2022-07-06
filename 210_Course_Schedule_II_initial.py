class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        0 -> 1
        0 -> 2
        1 -> 3
        2 -> 3
        
        0 -> [1,2]
        1 -> [3]
        2 -> [3]
        3 -> []
        post-order
    
        '''
        course_map = defaultdict(list)
        
        # Create the adjacency list
        for courses in prerequisites:
            course_b, course_a = courses[0], courses[1]
            course_map[course_a].append(course_b)
        
        res, visited = [], set()
        def dfs(course, course_map):
            # base case
            if course in visited: #cycle detected
                return False 
            if course_map[course] == []:
                res.append(course) if course not in res else None
                return True
            
            visited.add(course)
            
            for neighb_course in course_map[course]:
                if not dfs(neighb_course, course_map):
                    return False
            
            # after success
            course_map[course] = []
            res.append(course)
            visited.remove(course)
            
            return True
        
        for course_no in range(numCourses):
            if not dfs(course_no, course_map):
                return []
        
        return res[::-1] if res else [0]
            
        
        
        
        
        