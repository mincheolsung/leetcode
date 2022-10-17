class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cnt = [0]*26
        
        for c in sentence:
            index = ord(c) - ord('a') 
            cnt[index] += 1
            
        for i in range(26):
            if cnt[i] == 0:
                return False
        
        return True