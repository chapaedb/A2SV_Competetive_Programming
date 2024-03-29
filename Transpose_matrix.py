class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        transposed = []
        for j in range(cols):
            row = []
            for i in range(rows):
                row.append(matrix[i][j])
            transposed.append(row)

        return transposed
