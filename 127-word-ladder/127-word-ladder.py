class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = deque([[beginWord,1]])
        
        while q:
            word,d = q.popleft()
            if word == endWord:
                return d

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    candidate = word[:i] + c + word[i+1:]
                    if candidate in wordList:
                        q.append([candidate, d+1])
                        wordList.remove(candidate)
        return 0