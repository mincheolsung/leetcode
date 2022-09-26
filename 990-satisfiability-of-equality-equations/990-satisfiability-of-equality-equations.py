class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = {}
        keys = defaultdict(int)

        for equation in equations:
            [x,op1,op2,y] = list(equation)
            if x == y:
                if op1 == "!":
                    return False
                else:
                    continue

            if op1 == "=":
                if keys[x] == 0 and keys[y] == 0:
                    newSet = set([x,y])
                    newKey = len(equal)+1
                    equal[newKey] = newSet
                    keys[x] = newKey
                    keys[y] = newKey
                elif keys[x] != 0 and keys[y] == 0:
                    key = keys[x]
                    equal[key].add(y)
                    keys[y] = key
                elif keys[x] == 0 and keys[y] != 0:
                    key = keys[y]
                    equal[key].add(x)
                    keys[x] = key

                keyX,keyY = keys[x],keys[y]
                setX,setY = equal[keyX],equal[keyY]
                del equal[keyY]
                equal[keyX] = setX.union(setY)
                for key,value in keys.items():
                    if value == keyY:
                        keys[key] = keyX

        for equation in equations:
            [x,op1,op2,y] = list(equation)
            if op1 == "!":
                keyX,keyY = keys[x],keys[y]
                if keyX > 0 and x in equal[keyX] and keyY > 0 and y in equal[keyX]:
                    return False

        return True