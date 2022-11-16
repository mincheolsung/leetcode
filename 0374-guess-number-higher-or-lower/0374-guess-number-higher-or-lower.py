# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n

        while True:
            pi = low + (high - low)//2
            res = guess(pi)
            if res == 0:
                return pi
            elif res == 1:
                low = pi+1
            else:
                high = pi-1
    