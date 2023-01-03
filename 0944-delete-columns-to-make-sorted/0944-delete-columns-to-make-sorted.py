class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        
        grid = []
    
        for i in range(m):
            grid.append(list(strs[i]))
                    
        ans = 0
        for j in range(n):
            for i in range(m-1):
                if grid[i][j] > grid[i+1][j]:
                    ans+=1
                    break
        
        return ans