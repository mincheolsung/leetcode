class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = []
        for [l,r,h] in buildings:
            events.append([l,-h,r])
            events.append([r,0,0])
        events.sort()
        
        result = [[0,0]]
        maxHeight = [[0,float('inf')]] # h,r --> current maximum height
        for [x,h,r] in events:
            while maxHeight[0][1] <= x:
                heappop(maxHeight)
            
            if h: # update max height
                heappush(maxHeight, [h,r])

            if result[-1][1] != -maxHeight[0][0]: # if max height changes
                result.append([x, -maxHeight[0][0]])

        return result[1:]