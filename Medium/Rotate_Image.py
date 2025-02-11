class solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        A = matrix

        # Transpose
        for i in range(n):
            for j in range(i+1, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]

        # Reflection
        for i in range(n):
            for j in range(n //2):
                A[i][j], A[i][n-j-1] = A[i][n-j-1], A[i][j]