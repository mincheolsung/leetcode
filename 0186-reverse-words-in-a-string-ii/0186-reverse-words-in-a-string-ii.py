class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def myReverse(left: int, right: int):
            while left < right:
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1

        n = len(s)
        myReverse(0,n-1)
        i = 0
        start = 0
        while i < n:
            while i < n and s[i] != " ":
                i+=1
            myReverse(start, i-1)
            i+=1
            start = i