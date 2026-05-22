class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        m=len(matrix)
        n=len(matrix[0])
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        while(top<=bottom and left<=right):
            #move left to right on first row
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            #move top to bottom on last column
            for i in range(top+1,bottom+1):
                ans.append(matrix[i][right])
            #move right to left on last row
            if top<bottom:
                for i in range(right-1,left-1,-1):
                    ans.append(matrix[bottom][i])
            
            #move bottom to top on first column
            if left<right:
                for i in range(bottom-1,top,-1):
                    ans.append(matrix[i][left])

            #update all 4 to move to inner matrix spiral
            top+=1
            bottom-=1
            left+=1
            right-=1
        return ans

        
