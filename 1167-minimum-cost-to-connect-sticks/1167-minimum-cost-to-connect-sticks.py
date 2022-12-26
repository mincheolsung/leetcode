class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            temp = heappop(sticks) + heappop(sticks)
            heappush(sticks,temp)
            cost += temp

        return cost
        
        
        