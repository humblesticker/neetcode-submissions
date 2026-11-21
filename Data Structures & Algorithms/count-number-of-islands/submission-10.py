class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        compId = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] != "1": continue
                compId += 1

                stack = [ (r, c) ]
                while stack:
                    r, c = stack[-1]
                    grid[r][c] = compId

                    # explore up, down, left, right
                    if r-1 >= 0 and grid[r-1][c] == "1":stack.append((r-1, c))
                    elif r+1 < R and grid[r+1][c] == "1": stack.append((r+1, c))
                    elif c-1 >= 0 and grid[r][c-1] == "1": stack.append((r, c-1))
                    elif c+1 < C and grid[r][c+1] == "1": stack.append((r, c+1))
                    else: stack.pop()

        return compId

"""
stack based dfs
no function calls
"""