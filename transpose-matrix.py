class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transpose[j][i] = matrix[i][j]
        return transpose

    def transpose1(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, col = len(matrix), len(matrix[0])
        transpose = [[None]*rows for _ in range(col)]
        for i in range(rows):
            for j in range(col):
                transpose[j][i] = matrix[i][j]
        return transpose

    def transpose2(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)# Asterisk (*) is used for unpacking, like spread in javascript