class Solution: #Beats 98.99% in memory usage
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if mat == target:
                return True
            mat = self.rotOnce(mat)
        return False

    def rotOnce(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[-(j+1)][i] for j in range(len(row))] for i,row in enumerate(matrix)]
