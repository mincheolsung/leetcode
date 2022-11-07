class Solution:
    def maximum69Number (self, num: int) -> int:
        div = 10000
        while div > 0:
            if (num//div)%10 == 6:
                num += 3*div
                break
            div //= 10
        return num