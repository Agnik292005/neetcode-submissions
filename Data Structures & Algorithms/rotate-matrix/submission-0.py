class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        columns=len(matrix[0])
        for r in range(0,rows):
            for c in range(r,columns):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
        for row in matrix:
            start=0
            end=len(row)-1
            while(start<end):
                row[start],row[end]=row[end],row[start]
                start+=1
                end-=1
    
        
        