class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_r_zero = False
        first_c_zero = False

        for c in range(cols):
            if matrix[0][c] ==0:
                first_r_zero = True
                break
        for r in range(rows):
            if matrix[r][0] ==0:
                first_c_zero = True
                break
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c]==0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1,cols):
                    matrix[r][c] =0
        for c in range(1,cols):
            if matrix[0][c]==0:
                for r in range(1,rows):
                    matrix[r][c] =0
        if first_r_zero:
            for c in range(cols):
                matrix[0][c]=0
        if first_c_zero:
            for r in range(rows):
                matrix[r][0]=0
        
