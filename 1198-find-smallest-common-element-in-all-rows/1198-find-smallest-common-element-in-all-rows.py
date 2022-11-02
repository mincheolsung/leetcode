class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        cnt = Counter()
        m = len(mat)
        n = len(mat[0])
        
        for i in range(n):
            for j in range(m):
                key = mat[j][i]
                cnt[key] += 1
                if cnt[key] == m:
                    return key        

        return -1