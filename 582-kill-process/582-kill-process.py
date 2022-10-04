class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        ppid = { pid:ppid for (pid, ppid) in zip(pid, ppid) }
        marked = {p:0 for p in pid}

        if ppid[kill] == 0:
            return pid
        
        def dfs(pid: int, path: List[int]):
            if pid == 0 or marked[pid] == 1:
                for p in path:
                    marked[p] = 1;
                return

            if pid == kill or marked[pid] == 2:
                for p in path:
                    if p not in result:
                        marked[p] = 2
                        result.append(p)
                return

            path.append(pid)
            dfs(ppid[pid], path)

        result = [kill]
        for p in pid:
            dfs(p, [])

        return result