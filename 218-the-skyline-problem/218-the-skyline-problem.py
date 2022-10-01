class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = []
        for [l,r,h] in buildings:
            events.append([l,-h,r])
            events.append([r,0,0])
        events.sort()
        
        result = [[0,0]]
        #maxHeight[0]: [current maxHeight, boundary]
        maxHeight = [[0,float('inf')]]
        for [x,h,r] in events:
            while maxHeight[0][1] <= x: # pop out building which is end
                heappop(maxHeight)

            if h: # if it is a start of a building, push it into maxHeight since its height can be potentially max height
                heappush(maxHeight, [h,r])

            if result[-1][1] != -maxHeight[0][0]: # if max height chages from the previous key point
                result.append([x, -maxHeight[0][0]])

        return result[1:]