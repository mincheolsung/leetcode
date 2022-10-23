class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        mySet = set()

        result = []
        for num in nums:
            if num in mySet:
                result.append(num)
            else:
                mySet.add(num)

        for i in range(1,n+1):
            if i not in mySet:
                result.append(i)
                break

        return result