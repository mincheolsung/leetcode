class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if len(num) == 1:
            return num in "018"

        left = 0
        right = len(num)-1
        
        while left < right:
            if num[left] == '6' and num[right] == '9':
                left += 1
                right -= 1
            elif num[left] == '9' and num[right] == '6':
                left += 1
                right -= 1
            elif num[left] == '8' and num[right] == '8':
                left += 1
                right -= 1
            elif num[left] == '1' and num[right] == '1':
                left += 1
                right -= 1
            elif num[left] == '0' and num[right] == '0':
                left += 1
                right -= 1
            else:
                return False

        if left == right:
            return num[left] in "018"

        return True