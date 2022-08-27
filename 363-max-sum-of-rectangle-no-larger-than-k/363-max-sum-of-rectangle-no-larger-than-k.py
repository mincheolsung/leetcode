class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0
    
        rowSize = len(matrix)
        colSize = len(matrix[0])
        result = float('-inf')

        for i in range(colSize):
            sums = [0 for _ in range(rowSize)]
            for j in range(i, colSize):
                for row in range(rowSize):
                    sums[row] += matrix[row][j]
                    
                sortedSet = [0]
                curSum = 0
                tempMax = float('-inf')
                for item in sums:
                    curSum += item
                    index = bisect.bisect_left(sortedSet, curSum - k)
                    if index < len(sortedSet):
                        tempMax = max(tempMax, curSum - sortedSet[index])
                    bisect.insort(sortedSet, curSum)

                result = max(result, tempMax)

        return result
                