class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:                    
        def dfs(r:int, c:int):
            if (r,c) not in newStones:
                return

            newStones.remove((r,c))
            
            for nextC in row[r]:
                dfs(r,nextC)
            for nextR in col[c]:
                dfs(nextR,c)

        island = 0
        row = defaultdict(list)
        col = defaultdict(list)
        newStones = set([(r,c) for r,c in stones])

        for r,c in stones:
            row[r].append(c)
            col[c].append(r)
    
        for r,c in stones:
            if (r,c) in newStones:
                dfs(r,c)
                island+=1
        
        return len(stones) - island
        