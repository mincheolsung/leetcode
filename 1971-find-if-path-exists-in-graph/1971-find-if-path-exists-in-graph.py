class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for [s,d] in edges:
            graph[s].append(d)
            graph[d].append(s)

        visited = set()
        queue = [source]
        
        while queue:
            cur = queue.pop()
            if cur == destination:
                return True
            
            visited.add(cur)
            for next in graph[cur]:
                if next not in visited:
                    queue.append(next)

        return False
                
