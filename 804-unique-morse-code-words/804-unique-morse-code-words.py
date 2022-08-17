class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos = {
            'a':".-",
            'b':"-...",
            'c':"-.-.",
            'd':"-..",
            'e':".",
            'f':"..-.",
            'g':"--.",
            'h':"....",
            'i':"..",
            'j':".---",
            'k':"-.-",
            'l':".-..",
            'm':"--",
            'n':"-.",
            'o':"---",
            'p':".--.",
            'q':"--.-",
            'r':".-.",
            's':"...",
            't':"-",
            'u':"..-",
            'v':"...-",
            'w':".--",
            'x':"-..-",
            'y':"-.--",
            'z':"--.."
        }
        
        result = set()
        for word in words:
            temp = ""
            for c in word:
                temp += mos[c]
            result.add(temp)
            
        return len(result)