class Solution:
    def confusingNumber(self, n: int) -> bool:
        nums = {'0':'0',
                '1':'1',
                '6':'9',
                '8':'8',
                '9':'6'}
        s = list(str(n))
        if len(s) == 1:
            if s[0] in "69":
                return True
            else:
                return False
        
        left = 0
        right = len(s)-1
        
        while left <= right:
            if s[left] not in "01689" or s[right] not in "01689":
                return False
            s[left],s[right] = s[right],s[left]
            s[left] = nums[s[left]]
            s[right] = nums[s[right]]
            left+=1
            right-=1
        
        return n != int("".join(s))