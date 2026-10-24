class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        


        memo = {}
        def move(row, col):
            if (row,col) in memo:
                return memo[(row,col)]
            if row == 1 or col == 1:
                return 1
            memo[(row, col)] = move(row - 1, col) + move(row, col - 1)
            return memo[(row, col)]


        return move(m, n)