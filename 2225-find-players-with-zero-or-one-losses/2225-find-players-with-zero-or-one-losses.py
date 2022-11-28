class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [set(),set()]

        dict = {}
        for winner,loser in matches:
            if loser in dict:
                dict[loser].append(winner)
            else:
                dict[loser] = [winner]
    
        for winner,loser in matches:
            if winner not in dict:
                answer[0].add(winner)
            
            if len(dict[loser]) == 1:
                answer[1].add(loser)

        answer[0] = sorted(list(answer[0]))
        answer[1] = sorted(list(answer[1]))
        return answer