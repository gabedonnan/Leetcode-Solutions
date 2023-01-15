class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = [[matrix[-(j+1)][i] for j in range(len(row))] for i,row in enumerate(matrix)]
        for i,m in enumerate(x):
            for j,n in enumerate(m):
                matrix[i][j] = n
