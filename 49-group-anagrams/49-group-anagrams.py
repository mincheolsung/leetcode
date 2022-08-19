class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def is_anagram(str1, str2):
            if len(str1) != len(str2):
                return False

            str1 = sorted(str1)
            str2 = sorted(str2)
    
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    return False

            return True

        result = [[strs[0]]]
        myHash = collections.defaultdict(int)
        myHash[''.join(sorted(strs[0]))] = 1
    
        for str1 in strs[1:]:
            sorted_str = ''.join(sorted(str1))
            index = myHash[sorted_str]
            if index != 0:
                result[index-1].append(str1)
            else:
                myHash[sorted_str] = len(result) + 1
                result.append([str1])

        return result
                
                
                