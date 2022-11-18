class Solution:
    def isUgly(self, n: int) -> bool:
        while n > 0:
            if n/2 == int(n/2):
                n/=2
            elif n/3 == int(n/3):
                n/=3
            elif n/5 == int(n/5):
                n/=5
            elif n == 1:
                return True
            else:
                return False