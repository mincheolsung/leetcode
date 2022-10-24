class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        answer = 0
        for mask in range(1<<n):
            valid = True
            length = 0
            seen = set()
            for i in range(n):
                if ((mask >> i)&1) == 0:
                    continue;

                for letter in arr[i]:
                    if letter in seen:
                        valid = False
                        break;
                    seen.add(letter)
                    length += 1
                    
                if not valid:
                    break;
                
            if valid and length > answer:
                answer = length
                
        return answer
        
        
        