class Solution:
    def similarRGB(self, color: str) -> str:
        numbers = [0]*16
        
        for i in range(16):
            num = hex(i)[2:] + hex(i)[2:]
            numbers[i] = (i*17, num)

        def helper(color:str)->str:
            num = int(color, base=16)
            currentMin = float('inf')
            
            for i in range(16):
                if abs(num - numbers[i][0]) < currentMin:
                    currentMin = abs(num - numbers[i][0])
                    result = numbers[i][1]
            return result

        return "#" + helper(color[1:3]) + helper(color[3:5]) + helper(color[5:7])
    