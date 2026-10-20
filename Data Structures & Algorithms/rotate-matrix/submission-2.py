class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for i in range(N//2):
            for j in range(i, N-1-i):
                matrix[i][j], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[i][j]
                matrix[i][j], matrix[N-1-i][N-1-j] = matrix[N-1-i][N-1-j], matrix[i][j]
                matrix[i][j], matrix[N-1-j][i] = matrix[N-1-j][i], matrix[i][j]
                
        
"""
i, j -> j, N-1-i -> N-1-i, N-1-j -> N-1-j, i -> i, j

steps 
1. one cell [x]
2. one row [x]
3. 2 rows 


 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
"""