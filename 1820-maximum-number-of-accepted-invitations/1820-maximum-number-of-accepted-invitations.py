class Solution(object):
    def maximumInvitations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
                
        m = len(grid)
        n = len(grid[0])

        
        match = {}
        
        def find_girl(boy, asked):
            for girl in range(n):
                if grid[boy][girl] and girl not in asked:
                    asked.add(girl)
                    
                    if girl not in match or find_girl(match[girl], asked):
                        match[girl] = boy
                        return True

            return False
        
        for boy in range(m):
            find_girl(boy, set())
            
        return len(match)
                    
            
            