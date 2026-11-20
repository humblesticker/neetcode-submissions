class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        compId = 1

        def explore(r, c):
            if r < 0 or r >= R or c < 0 or c >= C: return # invlaid
            if grid[r][c] != "1": return # visited or water
            grid[r][c] = str(compId)

            # explore up, down, left, right
            explore(r-1, c)
            explore(r+1, c)
            explore(r, c-1)
            explore(r, c+1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] != "1": continue
                compId += 1
                explore(r, c)
                
        return compId-1

"""
test
[0] - ok
[1] - ok

# of connected comp
dfs: mark first as 2, 3, 4 and so on 
return count-1

if 1 you can move and mark as current compId
else you can not move, skip

recursive, in-place tracking
"""