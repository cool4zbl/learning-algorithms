class Solution:
    """
        90 degree clockwise rotation -
        0. mirror/transpose the diagonal from top-left to bottom-right.
        1. reverse each row of the matrix

        90 degree counterclockwise rotation -
        0. mirror/transpose the diagonal from top-right to bottom-left.
        1. reverse each row of the matrix

    """
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # transpose
        for i in range(n):
            for j in range(i+1, n): # j starts at `i+1`
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # flip horizontally
        for i in range(n):
            for j in range(n // 2): # j ends at `n//2`
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
