class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for i,room in enumerate(rooms):
            for key in room:
                graph[i].append(key)
                
        queue = [0]
        visited = set()
        while queue:
            cur = queue.pop()
            visited.add(cur)
            
            if len(visited) == len(rooms):
                return True
            
            for next in graph[cur]:
                if next not in visited:
                    queue.append(next)
            
        return False
        
        