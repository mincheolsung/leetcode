class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = []
        
        if not graph:
            return result

        def dfs(temp, start):
            if temp[-1] == len(graph)-1:
                result.append(temp[:])
                
            for node in graph[start]:
                temp.append(node)
                dfs(temp, node)
                temp.pop()
                
        dfs([0], 0)        
        
        return result
                
                