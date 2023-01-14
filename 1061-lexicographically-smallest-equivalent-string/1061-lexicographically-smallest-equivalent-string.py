class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}
        
        def find(x: str)->str:
            if x not in UF:
                UF[x] = x
                
            if x != UF[x]:
                UF[x] = find(UF[x])
            
            return UF[x]
        
        def union(s1: str, s2: str):
            root1 = find(s1)
            root2 = find(s2)
            
            if root1 < root2:
                UF[root2] = root1
            else:
                UF[root1] = root2
                
        
        for i in range(len(s1)):
            union(s1[i],s2[i])
            
        ans = []
        for i in range(len(baseStr)):
            ans.append(find(baseStr[i]))
        
        
        return "".join(ans)
        