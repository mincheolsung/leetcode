class Solution:
    def maximum69Number (self, num: int) -> int:
        numStr = list(str(num))
        for i in range(len(numStr)):
            if numStr[i] == '6':
                numStr[i] = '9'
                break

        return int(''.join(numStr))