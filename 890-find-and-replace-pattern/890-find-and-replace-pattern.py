class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        def is_matched(word, pattern):
            if len(pattern) == 1:
                return True
            
            d = {}
            
            for i in range(0,len(pattern)):
                if pattern[i] not in d:
                    if word[i] in d.values():
                        return False
                    else:
                        d[pattern[i]] = word[i]
                else:
                    if d[pattern[i]] != word[i]:
                        return False
            
            return True
        
        result = []
        for i in range(0,len(words)):
            if is_matched(words[i], pattern) is True:
                result.append(words[i])
        
        return result