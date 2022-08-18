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
        if len(self.myMap) < len(vec.myMap):
            map1, map2 = self.myMap, vec.myMap
        else:
            map2, map1 = self.myMap, vec.myMap
        
        items = map1.items()
        for i, value in items:
            ans += value * map2[i]
            
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)