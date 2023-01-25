class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        d1 = [-1]*len(edges)
        d2 = [-1]*len(edges)

        q = [(node1,0)]
        visited = set()
        while q:
            node,d = q.pop()
            if node == -1:
                break
            d1[node] = d
            visited.add(node)
            if edges[node] not in visited:
                q.append((edges[node],d+1))
        
        q = [(node2,0)]
        visited = set()
        while q:
            node,d = q.pop()
            if node == -1:
                break
            d2[node] = d
            visited.add(node)
            if edges[node] not in visited:
                q.append((edges[node],d+1))

        ans = -1
        mini = float('inf')
        for i in range(len(d1)):
            if d1[i] == -1 or d2[i] == -1:
                continue
            if mini > max(d1[i],d2[i]):
                mini = max(d1[i],d2[i])
                ans = i

        return ans