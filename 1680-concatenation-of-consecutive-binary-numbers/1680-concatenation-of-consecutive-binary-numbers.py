class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 1
        for num in range(2, n+1):
            swift = int(log(num,2)) + 1
            result = result << swift
            result += num
            result %= 1000000007

        return result