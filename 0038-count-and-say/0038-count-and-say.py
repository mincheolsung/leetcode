class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        i = 0
        temp = list(self.countAndSay(n-1))
        l = len(temp)
        result = ""
        while i < l:
            cnt = 1
            while i+1 < l and temp[i] == temp[i+1]:
                i+=1
                cnt+=1

            result += str(cnt)
            result += temp[i]
            i+=1

        return result
        
        
        