class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        compId = 0

        def explore(r, c):
            if grid[r][c] != "1": return # visited or water
            grid[r][c] = compId

            # explore up, down, left, right
            if r-1 >= 0: explore(r-1, c)
            if r+1 < R: explore(r+1, c)
            if c-1 >= 0: explore(r, c-1)
            if c+1 < C: explore(r, c+1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] != "1": continue
                compId += 1
                explore(r, c)
                
        return compId

"""
stack based dfs
no function calls
"""