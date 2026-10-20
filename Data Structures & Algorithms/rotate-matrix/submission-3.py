class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        def rotate(i, j):
            prev = matrix[i][j]
            for _ in range(4): 
                i, j = j, N-1-i
                matrix[i][j], prev = prev, matrix[i][j]
                
        for i in range(N//2):
            for j in range(i, N-1-i):
                rotate(i, j)
                
        
"""

"""