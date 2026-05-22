class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows=matrix.length;
        int columns=matrix[0].length;
        for(int i=0;i<rows;i++){
            if(matrix[i][0]<=target && matrix[i][columns-1]>=target){
                int start=0;
                int end=columns-1;
                while(start<=end){
                    int mid=start+(end-start)/2;
                    if(target>matrix[i][mid]){
                        start=mid+1;
                    }else if(target<matrix[i][mid]){
                        end=mid-1;
                    }else{
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
