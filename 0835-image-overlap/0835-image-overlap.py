class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        point1 = []
        point2 = []
        seen = defaultdict(int)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    point1.append((i,j))
                if img2[i][j] == 1:
                    point2.append((i,j))
    
        ans = 0
        for p1 in point1:
            for p2 in point2:
                p3 = (p2[0]-p1[0],p2[1]-p1[1])
                seen[p3] += 1
                ans = max(ans, seen[p3])
        return ans