class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        
        def helper(start:int) -> bool:
            stack = [(start,colors[start])]
            
            while stack:
                cur,color = stack.pop()
                if cur in colors and colors[cur] != color:
                    return False

                colors[cur] = color
                visited.add(cur)

                for next in graph[cur]:
                    if next not in visited:
                        stack.append((next,color^1))

            return True

        graph = defaultdict(list)
        colors = defaultdict(int)
        starts = []
        visited = set()

        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
            starts.append(i)
            starts.append(j)
            
        for start in starts:
            if start not in visited:
                if helper(start) == False:
                    return False

        return True