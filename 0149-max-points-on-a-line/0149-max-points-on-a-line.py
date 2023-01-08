class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1

        pairs = set()
        myMap = defaultdict(set)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if (j,i) not in pairs:
                    pairs.add((i,j))

        for i,j in pairs:
            x1,y1 = points[i]
            x2,y2 = points[j]

            if x2-x1 == 0:
                myMap[(float('inf'), x1)].add((x1,y1))
                myMap[(float('inf'), x1)].add((x2,y2))
            else:
                myMap[((y2-y1)/(x2-x1), ((y1*x2)-(y2*x1))/(x2-x1))].add((x1,y1))
                myMap[((y2-y1)/(x2-x1), ((y1*x2)-(y2*x1))/(x2-x1))].add((x2,y2))

        ans = 0
        for item in myMap.values():
            ans = max(ans, len(item))

        return ans