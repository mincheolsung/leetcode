class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(list(word)))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        result = [group for group in groups.values()]
        return result