class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rowSize = len(mat)
        colSize = len(mat[0])
        
        
        array = [deque([]) for _ in range(rowSize + colSize - 1)]
        array = deque(array)
        
        offset = colSize - 1
        
        for r in range(rowSize):
            for c in range(colSize):
                index = r - c + offset
                array[index].append(mat[r][c])

        for i in range(len(array)):
            arr = array.popleft()
            array.append(deque(sorted(arr)))
            
        for r in range(rowSize):
            for c in range(colSize):
                index = r - c + offset
                mat[r][c] = array[index].popleft()
                
        return mat
                
        
            