class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        frequency = [0]*26
        counter = 26
        for c in sentence:
            index = ord(c) - ord('a') 
            if frequency[index] == 0:
                counter-=1
            frequency[index] += 1

        return True if counter == 0 else False