class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(ss:str)->bool:
            if not ss:
                return False
            return ss[:] == ss[::-1]
        
        def backtrack(ss: str, temp:List[str]):
            if not ss:
                ans.append(temp[:])
                return

            for i in range(len(ss)+1):
                sss = ss[:i]
                if isPalindrome(sss):
                    temp.append(sss)
                    backtrack(ss[i:],temp)
                    temp.pop()

        ans = []
        backtrack(s,[])
        
        return ans                