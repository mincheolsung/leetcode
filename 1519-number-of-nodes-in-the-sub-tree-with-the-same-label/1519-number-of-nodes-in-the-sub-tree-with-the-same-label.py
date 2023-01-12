class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node:int)->Counter:
            res = Counter()
            if node in visited:
                return res

            visited.add(node)

            for child in graph[node]:
                res += dfs(child)

            res[labels[node]] += 1
            ans[node] = res[labels[node]]
            return res

        graph = defaultdict(list)
        ans = [0]*n
        label = defaultdict(int)
        
        for v,e in edges:
            graph[v].append(e)
            graph[e].append(v)
            
        visited = set()

        dfs(0)

        return ans