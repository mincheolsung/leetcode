class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def is_follow(data: int) -> bool:
            if 128 <= data <= 191:
                return True
            else:
                return False
            
        def numByte(data: int) -> int:
            if data <= 127:
                return 1
            elif 192 <= data <= 223:
                return 2
            elif 224 <= data <= 239:
                return 3
            elif 240 <= data <= 247:
                return 4
            else:
                return 0
            
        byte = 0
        while data:
            num = data.pop()
            if is_follow(num):
                byte+=1
            else:
                if numByte(num) != byte + 1:
                    return False
                else:
                    byte = 0
            
        return True if byte == 0 else False
                
        
        