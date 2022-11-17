class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        result = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)

        x1 = max(ax1,bx1)
        x2 = min(ax2,bx2)
        y1 = max(ay1,by1)
        y2 = min(ay2,by2)    
        
        if x1 > x2 or y1 > y2:
            return result

        overlap = (x2-x1)*(y2-y1)
        
        return result - overlap