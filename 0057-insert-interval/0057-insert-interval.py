class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = deque(sorted(intervals))

        ret = [intervals.popleft()]
        
        while intervals:
            x1,y1 = ret.pop()
            x2,y2 = intervals.popleft()
            # x1 y1
            #       x2 y2
            if y1 < x2:
                ret.append([x1,y1])
                ret.append([x2,y2])
            # x1  y1
            #   x2  y2
            elif x2 <= y1 < y2:
                ret.append([x1,y2])
            # x1     y1
            #   x2 y2
            else:
                ret.append([x1,y1])

        return ret        