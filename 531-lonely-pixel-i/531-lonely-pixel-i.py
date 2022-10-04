class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        rowMarker = [0]*m
        colMarker = [0]*n
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    rowMarker[i] += 1
                    colMarker[j] += 1
                    
        ans = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if rowMarker[i] == 1 and colMarker[j] == 1:
                        ans+=1

        return ans