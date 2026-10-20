class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        def rotate(i, j):
            ni, nj = j, N-1-i
            for _ in range(3): 
                matrix[ni][nj], matrix[i][j] = matrix[i][j], matrix[ni][nj]
                ni, nj = nj, N-1-ni
                
        for i in range(N//2):
            for j in range(i, N-1-i):
                rotate(i, j)
                
        
"""

"""