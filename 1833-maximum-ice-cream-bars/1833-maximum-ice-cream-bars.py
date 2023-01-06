class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        presum = [0]*len(costs)
        presum[0] = costs[0]
        for i in range(1, len(costs)):
            presum[i] = presum[i-1] + costs[i]
            
        return bisect_right(presum, coins)