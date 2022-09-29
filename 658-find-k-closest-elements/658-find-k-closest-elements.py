class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]

        diff = {}
        for num in arr:
            if abs(num-x) in diff:            
                diff[abs(num-x)].append(num)
            else:
                diff[abs(num-x)] = [num]
                

        temp = sorted(diff.items())
        
        result = []
        for _,v in temp:
            result += v
        print(result)
        return sorted(result[:k])
        