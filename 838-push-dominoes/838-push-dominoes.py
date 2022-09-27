class Solution:
    def pushDominoes(self, d: str) -> str:
        n = len(d)
        r = [0]*n
        l = [0]*n
        result = [""]*n

        if d[0] == "R":
            r[0] = 1
        
        if d[-1] == "L":
            l[-1] = 1

        for i in range(1, n):
            if d[i] == "R":
                r[i] = 1
            elif d[i] == "L":
                r[i] = 0
            elif r[i-1] > 0:
                r[i] = r[i-1] + 1
                
        for i in range(n-2,-1,-1):
            if d[i] == "L":
                l[i] = 1
            elif d[i] == "R":
                l[i] = 0
            elif l[i+1] > 0:
                l[i] = l[i+1] + 1

        for i in range(n):
            if r[i] > 0 and l[i] == 0:
                result[i] = 'R'
            elif r[i] == 0 and l[i] > 0:
                result[i] = 'L'
            elif r[i] == l[i]:
                result[i] = '.'
            elif r[i] < l[i]:
                result[i] = 'R'
            elif r[i] > l[i]:
                result[i] = 'L'

        return "".join(result)