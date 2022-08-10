class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        
        digits = ["0","1","2","3","4","5","6","7","8","9"]

        result = []

        def backtrack(index, num):
            if index == n:
                if num[0] != "0":
                    for i in range(0,n-1):
                        if abs(int(num[i])-int(num[i+1])) != k:
                            return
                    result.append(int(num))
                return
             
            for i in range(0, 10):
                if len(num) > 0:
                    if abs(int(num[-1]) - int(digits[i])) != k:
                        continue
    
                num += digits[i]
                backtrack(index+1, num)
                num = num[:-1]

        backtrack(0,"")
        
        return result
        
            
            