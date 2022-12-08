class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        nodes = set(range(n))

        def dfs(node:int):   
            if node not in nodes:
                return
            nodes.remove(node)
            for node in graph[node]:
                dfs(node)
            
        ans = 0
        for node in range(n):
            if node in nodes:
                ans+=1
                dfs(node)
        
        return ans
            
            
            
        