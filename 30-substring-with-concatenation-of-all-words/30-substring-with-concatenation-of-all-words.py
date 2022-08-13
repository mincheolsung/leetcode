class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        lenWords = len(words[0]) * len(words)
        
        def compare(s, words):
            temp = []
            for _ in range(len(words)):
                temp.append(s[:len(words[0])])
                s = s[len(words[0]):]
            
            temp.sort()
            words.sort()
            
            a = "".join(temp)
            b = "".join(words)
            
            if a == b:
                return True;
            else:
                return False;
                
        result = []
        for i in range(0, len(s)):
            if compare(s[i:i+lenWords], words):
                result.append(i)
                
        return result
        