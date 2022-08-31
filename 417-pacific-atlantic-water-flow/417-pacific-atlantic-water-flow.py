class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        result = []
        
        def dfs(r: int, c: int, reachable: set):
            nonlocal m
            nonlocal n
            
            reachable.add((r,c))
            
            for moveR, moveC in ((0,1),(1,0),(0,-1),(-1,0)):
                newR = r + moveR
                newC = c + moveC
                if newR < 0 or newC < 0 or newR > m-1 or newC > n-1:
                    continue
                
                if (newR,newC) in reachable:
                    continue
                    
                if heights[r][c] > heights[newR][newC]:
                    continue
                    
                dfs(newR,newC,reachable)
                
                
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
            
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)
            
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i,j])
                    
        return result
                    