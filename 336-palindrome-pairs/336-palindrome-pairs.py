class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word:str)->bool:
            return word == word[::-1]
        
        words = {w:i for i,w in enumerate(words)}
        result = []
        
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                prefix = word[:j]
                suffix = word[j:]

                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in words:
                        result.append([words[back],k])

                if j != n and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back != word and back in words:
                        result.append( [ k, words[back]])

        return result
        