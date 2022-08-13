class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        len_of_word = len(words[0])
        num_of_word = len(words)
        len_of_words = len_of_word * num_of_word
        
        def compare(s, words):
            temp = []
            for i in range(0, len_of_words, len_of_word):
                temp.append(s[i:i+len_of_word])
    
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
            if compare(s[i:i+len_of_words], words):
                result.append(i)
                
        return result
        