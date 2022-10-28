class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        point1 = []
        point2 = []
        num1 = 0
        num2 = 0
        seen = defaultdict(int)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    point1.append((i,j))
                    num1+=1
                if img2[i][j] == 1:
                    point2.append((i,j))
                    num2+=1
    
        ans = 0
        for t1 in point1:
            for t2 in point2:
                t3 = (t2[0]-t1[0],t2[1]-t1[1])
                seen[t3] += 1
                ans = max(ans, seen[t3])
        return ans