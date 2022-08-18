class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = collections.Counter(arr)
        freq = count.values()
        freq.sort(reverse=True)
        
        length = sum(freq)
        target = sum(freq)/2
        i = 0
        result = 0
        while i < len(freq):
            length -= freq[i]
            if length > target:
                result+=1
                i+=1
            else:
                result+=1
                return result