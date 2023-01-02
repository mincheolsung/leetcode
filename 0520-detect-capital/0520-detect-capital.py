class Solution:
    def detectCapitalUse(self, word: str) -> bool:        
        def isCapital(s: str):
            return (ord('A') <= ord(s) <= ord('Z'))
        
        numCap = 0
        for i in range(len(word)):
            if isCapital(word[i]):
                numCap+=1
        
        if isCapital(word[0]):
            if numCap == len(word) or numCap == 1:
                return True
            else:
                return False
        else:
            if numCap > 0:
                return False
            else:
                return True
        

            