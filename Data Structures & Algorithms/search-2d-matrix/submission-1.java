class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int start=0;
        int end=(matrix.length*matrix[0].length)-1;
        int columns=matrix[0].length;
        while(start<=end){
            int mid=start+(end-start)/2;
            if(matrix[mid/columns][mid%columns]==target){
                return true;
            }else if(matrix[mid/columns][mid%columns]>target){
                end=mid-1;
            }else{
                start=mid+1;
            }
        }
        return false;
    }
}
