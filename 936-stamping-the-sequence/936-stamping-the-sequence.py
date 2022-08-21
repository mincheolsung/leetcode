class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """

        s = len(stamp)
        t = len(target)
        stamp = list(stamp)
        target = list(target)
        result = []
        
        def reverseStamp(i):
            didStamp = False
            for j in range(s):
                if target[i+j] == "?":
                    continue
                elif target[i+j] != stamp[j]:
                    return False
                elif target[i+j] == stamp[j]:
                    didStamp = True

            if didStamp:
                target[i:i+s] = ["?"]*s
                result.append(i)

            return didStamp
        
        loop = True
        i = 0
        while loop:
            loop = False
            for i in range(t-s+1):            
                loop |= reverseStamp(i)

        if target == ["?"]*t:
            return result[::-1]
        else:
            return []
        
    