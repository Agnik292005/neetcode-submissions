class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        ans=[[0]*n for i in range(m)]
        for r in range(n):
            for c in range(m):
                ans[c][r]=matrix[r][c]
        return ans