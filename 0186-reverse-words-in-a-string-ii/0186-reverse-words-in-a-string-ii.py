class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def myInsert(c:str):
            index = s.find("*")
            s.insert(index, c)
            
        n = len(s)
        end = n
        start = 0
        for i in range(n):
            if s[i] == " ":
                start = i

        start += 1
        s.append(" ")

        while start > 0:
            temp = end
            while True:
                c = s.pop(0)
                s.insert(temp, c)
                start -= 1
                end -= 1
                if c == " ":
                    break
        s.pop()
        return s
                
        