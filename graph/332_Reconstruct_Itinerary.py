class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        Time - Complexity: O(V + E^2) due to backtracking
        Space - Complexity: O(E)
        '''

        tickets.sort() # to get into lexical order
        # build the graph
        graph = collections.defaultdict(list)
        for ticket1, ticket2 in tickets:
            graph[ticket1].append(ticket2)
        
        res = ["JFK"]
        def dfs(src, selection_list):
            if len(selection_list) == len(tickets):
                res.extend(selection_list)
                return True
            # we need to update the graph
            tmp_adj_list = graph[src]
            for i, neighb_node in enumerate(tmp_adj_list):
                # make a selection
                selection_list.append(neighb_node)
                # remove from possible paths
                graph[src].pop(i)
                if dfs(neighb_node, selection_list):
                    return True
                # remove from selection_list
                selection_list.pop()
                # add back into possible paths
                graph[src].insert(i, neighb_node)
            return False
        dfs("JFK", [])
        return res
        
            

        
        