class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        '''
        def findSum(colSum: List[int], k: int) -> int:
            sortedSet = [0]
            currentSum = 0
            maxSum = -sys.maxsize - 1

            for s in colSum:
                currentSum += s
                left = bisect.bisect_left(sortedSet, currentSum-k)
                if left < len(sortedSet):
                    maxSum = max(maxSum, currentSum - sortedSet[left])
                bisect.insort(sortedSet, currentSum)
                
            return maxSum

        if not matrix:
            return 0
        
        sizeRow = len(matrix)
        sizeCol = len(matrix[0])
        result = -sys.maxsize-1

        for i in range(sizeCol):
            colSum = [0]*sizeRow
            for j  in range(i, sizeCol):
                for r in range(sizeRow):
                    colSum[r] += matrix[r][j]
                    
            result = max(result, findSum(colSum, k))
            
        return result
        '''
        if not matrix:  return 0
        
        res = float('-inf')
        rows, columns = len(matrix), len(matrix[0])
        for i in range(columns):
            sums = [0 for _ in range(rows)]
            for j in range(i, columns):
                for r in range(rows):
                    sums[r] += matrix[r][j]

                # find the largest sum of a subarray which is no more than K
                import bisect
                cum_sum = [0]
                cum, max_sum = 0, float('-inf')
                for item in sums:
                    cum += item
                    left = bisect.bisect_left(cum_sum, cum - k)
                    if left < len(cum_sum):
                        max_sum = max(max_sum, cum - cum_sum[left])
                    bisect.insort(cum_sum, cum)

                res = max(res, max_sum)

        return res