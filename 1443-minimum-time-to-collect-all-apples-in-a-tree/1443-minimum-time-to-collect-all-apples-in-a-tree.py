class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        ans = 0

        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = set()
        
        def helper(root: int)->int:
            if root in visited:
                return 0
            visited.add(root)
            sec = 0
            for next in graph[root]:
                sec += helper(next)

            if sec > 0:
                return sec + 2
            else:
                if hasApple[root]:
                    return 2
                else:
                    return 0
    
        return max(helper(0) - 2, 0)