class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        myZip = list(zip(plantTime, growTime))
        myZip.sort(key = lambda x:-x[1])
        
        current = 0
        answer = 0
        for plant,grow in myZip:
            current += plant
            answer = max(answer, current + grow)
    
        return answer