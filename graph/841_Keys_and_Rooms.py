class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        if 1 of the graph isnt visisted then we have to answer no.
        O( E + V) since every node is visited at most once
        '''
        no_of_rooms = len(rooms)
        graph = {}
        for i, list_rooms in enumerate(rooms):
            graph[i] = list_rooms
        seen = set()
        def dfs(cur_node):
            if cur_node in seen:
                return
            seen.add(cur_node)
            for neighb_node in graph[cur_node]:
                dfs(neighb_node)
        dfs(0)
        return len(seen) == no_of_rooms