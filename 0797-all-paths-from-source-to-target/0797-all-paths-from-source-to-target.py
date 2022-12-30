class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        final = len(graph)-1
        graphs = defaultdict(list)
        for i,dest in enumerate(graph):
            graphs[i] = dest
                    
        q = [(0,[0])]
        ans = []

        while q:
            src,temp = q.pop()

            if not temp:
                temp = []
            
            if src == final:
                ans.append(temp[:])
                continue
                
            for dst in graphs[src]:
                q.append((dst, temp + [dst]))    

        return ans