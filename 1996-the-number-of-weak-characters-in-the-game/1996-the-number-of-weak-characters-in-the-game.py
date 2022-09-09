class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        result = 0
        currentMax = 0
        for i in range(len(properties)-1, -1, -1):
            if properties[i][1] < currentMax:
                result+=1
            else:
                currentMax = properties[i][1]
        
        return result