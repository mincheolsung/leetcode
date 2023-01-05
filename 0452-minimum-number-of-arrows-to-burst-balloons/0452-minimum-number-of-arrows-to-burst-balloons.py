class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[1])
        
        ans = 1
        firstEnd = points[0][1]

        for start,end in points:
            if firstEnd < start:
                ans+=1
                firstEnd = end
        
        return ans
            
            

            
        