class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        myHashMap = defaultdict(int)
        answer = 0
        alone = 0
        
        for word in words:
            if word[0] == word[1]:
                if myHashMap[word] > 0:
                    alone-=1
                    myHashMap[word] -= 1
                    answer += 4
                else:
                    alone+=1
                    myHashMap[word] += 1
            else:
                if myHashMap[word[-1::-1]] > 0:
                    myHashMap[word[-1::-1]] -= 1
                    answer += 4
                else:
                    myHashMap[word] += 1

        if alone > 0:
            answer += 2
                
        return answer