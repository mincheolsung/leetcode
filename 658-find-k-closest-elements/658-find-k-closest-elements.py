class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]

        diff = [[] for _ in range(20000)]

        for num in arr:  
            diff[abs(num-x)].append(num)

        result = []
        for temp in diff:
            n = len(temp)
            if n > 0:
                result += temp
            if n > k:
                break
        return sorted(result[:k])
        