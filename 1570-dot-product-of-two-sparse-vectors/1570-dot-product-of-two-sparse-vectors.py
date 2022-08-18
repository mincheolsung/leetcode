class SparseVector:    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.myMap = defaultdict(int)
        for i,value in enumerate(nums):
            if value != 0:
                self.myMap[i] = value

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        ans = 0
        items = self.myMap.items()
        for i, value in items:
            ans += value * vec.myMap[i]
            
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)