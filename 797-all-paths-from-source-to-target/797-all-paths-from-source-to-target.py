class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = [] 
        q = deque()
        q.append([0])
        
        while q:
            path = q.popleft()
            if path[-1] == len(graph)-1:
                result.append(path)
            else:
                for node in graph[path[-1]]:
                    q.append(path + [node])
    
        return result
                
                