class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = len(s)-1
        
        while i >= 0:
            if s[i] == 'I':
                result+=1
            elif s[i] == 'V':
                if i != 0 and s[i-1] == 'I':
                    result+=4
                    i-=1
                else:
                    result+=5
            elif s[i] == 'X':
                if i != 0 and s[i-1] == 'I':
                    result+=9
                    i-=1
                else:
                    result+=10
            elif s[i] == 'L':
                if i != 0 and s[i-1] == 'X':
                    result+=40
                    i-=1
                else:
                    result+=50
            elif s[i] == 'C':
                if i != 0 and s[i-1] == 'X':
                    result+=90
                    i-=1
                else:
                    result+=100
            elif s[i] == 'D':
                if i != 0 and s[i-1] == 'C':
                    result+=400
                    i-=1
                else:
                    result+=500
            elif s[i] == 'M':
                if i != 0 and s[i-1] == 'C':
                    result+=900
                    i-=1
                else:
                    result+=1000    
            i-=1
            
        return result
            
                