class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def compare(p1:tuple, p2:List[int], p3:List[int])->int:
            x1,y1 = p1
            x2,y2 = p2
            x3,y3 = p3
            
            if (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2) > 0:
                return 1
            elif (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2) < 0:
                return -1
            else:
                return 0
        
        
        trees.sort()
        low = []
        high = []
        
        for point in trees:
            while len(low) > 1 and compare(low[-2], low[-1], point) < 0:
                low.pop()
                
            while len(high) > 1 and compare(high[-2], high[-1], point) > 0:
                high.pop()
                
            low.append(tuple(point))
            high.append(tuple(point))

        result = set(low+high)
        return result