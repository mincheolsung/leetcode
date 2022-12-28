class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapify(piles)

        for _ in range(k):
            pile = heappop(piles)
            heappush(piles, floor(pile/2))
            
        return -sum(piles)