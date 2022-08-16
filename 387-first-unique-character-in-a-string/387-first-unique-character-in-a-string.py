class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.Counter(s)       
        for i,val in enumerate(s):
            if cnt[val] == 1:
                    return i
        
        return -1