class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Phase 1: Mark rows and columns
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        first_row_zero = True
                    if j == 0:
                        first_col_zero = True

        # Phase 2: Zero inner matrix using markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Phase 3: Zero first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Phase 4: Zero first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
