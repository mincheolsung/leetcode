class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 1
        for num in range(2, n+1):
            result = ((result << (int(log(num,2)) + 1)) + num) % 1000000007
        return result