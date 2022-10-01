class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = []
        for [l,r,h] in buildings:
            events.append([l,-h,r])
            events.append([r,0,0])
        events.sort()
        
        
        result = [[0,0]]
        live = [[0,float('inf')]] # h,r
        for [x,h,r] in events:
            while live[0][1] <= x:
                heappop(live)
            
            if h:
                heappush(live, [h,r])

            if result[-1][1] != -live[0][0]:
                result.append([x, -live[0][0]])
                
        return result[1:]