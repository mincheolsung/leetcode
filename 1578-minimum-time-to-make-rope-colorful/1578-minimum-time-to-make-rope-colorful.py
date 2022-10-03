class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        time = [[neededTime[0]]]

        for i in range(1,n):
            if colors[i] == colors[i-1]:
                heappush(time[-1], neededTime[i])
            else:
                time.append([neededTime[i]])

        remove = []
        for temp in time:
            while len(temp) > 1:
                remove.append(heappop(temp))

        return sum(remove)
            
         