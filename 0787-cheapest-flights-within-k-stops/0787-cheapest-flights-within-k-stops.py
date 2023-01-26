class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[1],flight[2]))
        
        q = deque([(0, src, 0)])
        ans = [float('inf')]*n

        while q:
            price,node,d = q.popleft()
            if d <= k+1 and price < ans[node]:
                ans[node] = price
                for next,newPrice in graph[node]:
                    q.append((price + newPrice, next, d+1))

        return ans[dst] if ans[dst] != float('inf') else -1