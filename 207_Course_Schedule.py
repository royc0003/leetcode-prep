class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        (1) create a directed adjacency list
        (2) create a dfs
            - base case: (1) check if no cycle
                         (2) check if has completed all pre-requisites
            - fail case:
                        (1) if returning statement is fasle just return
            - success case:
                        (1) ensure pre-requisites are empty
                        (2) return True
        '''
        adj_list = defaultdict(list)
        
        # {preq_course: [all desired courses]}
        for courses in prerequisites:
            desired_course, preq_course = courses[0], courses[1]
            adj_list[preq_course].append(desired_course)
        
        visited_set = set()
        
        def dfs(course_no):
            # there's cycle
            if course_no in visited_set:
                return False
            # if no pre-req courses, we can return
            if adj_list[course_no] == []:
                return True
            # add to visited
            visited_set.add(course_no)
            
            # go through neighbouring courses
            for neighb_course in adj_list[course_no]:
                res = dfs(neighb_course)
                if res == False:
                    return False
            # remove from visited list
            visited_set.remove(course_no)
            # set the pre_req to emtpy
            adj_list[course_no] = []
            return True
                
            
        for course_no in range(numCourses):
            res = dfs(course_no)
            if not res: return False
        return res
        