class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def parse(s: str) -> (str, str):
            content = s.split("(")
            return (content[0], content[1].split(")")[0])

        dict = {}
        result = []

        for s in paths:
            s = deque(s.split())
            path = s.popleft()
            while s:
                name, content = parse(s.popleft())
                if content in dict:
                    dict[content].append(path+"/"+name)
                else:
                    dict[content] = [path+"/"+name]

        for (key,value) in dict.items():
            if len(value) > 1:
                result.append(value)

        return result