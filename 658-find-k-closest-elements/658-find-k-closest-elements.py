class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = sorted(arr, key=lambda num:abs(x-num))
        return sorted(result[:k])