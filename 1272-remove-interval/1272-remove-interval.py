class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        answer = []
        
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if start < toBeRemoved[0] and toBeRemoved[1] < end:
                answer.append([start, toBeRemoved[0]])
                answer.append([toBeRemoved[1], end])
            elif toBeRemoved[0] <= start and end <= toBeRemoved[1]:
                continue
            elif start < toBeRemoved[0] <= end:
                answer.append([start, toBeRemoved[0]])  
            elif start < toBeRemoved[1] <= end:
                answer.append([toBeRemoved[1], end])
            else:
                answer.append([start, end])

        return answer
                