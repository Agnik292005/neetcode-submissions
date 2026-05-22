class Solution {
    public int maxArea(int[] heights) {
        //two pointers approach
        int max=0;
        int r=heights.length-1;
        int l=0;
        int area=0;
        while(l<r){
            area=(r-l)*Math.min(heights[r],heights[l]);
            max=Math.max(area,max);
            if(heights[r]>heights[l]){
                l++;
            }else{
                r--;
            }
        }
        return max;
        
    }
}
