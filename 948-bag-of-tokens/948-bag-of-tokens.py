class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        def helper(tokens: List[int], power: int):
            if len(tokens) == 0:
                return
            res = 0
            balance = power
            for token in tokens:
                if balance >= token:
                    res += 1
                    balance -= token
                else:
                    break

            answer[0] = max(answer[0], res)
            helper(tokens[1:-1], power + tokens[-1] - tokens[0])
        
        if len(tokens) < 1:
            return 0
        
        tokens.sort()
        
        if power < tokens[0]:
            return 0

        answer = [0]
        helper(tokens, power)
        
        return answer[0]
    
    
        