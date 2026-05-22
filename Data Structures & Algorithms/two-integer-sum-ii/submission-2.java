class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start=0;
        int end=numbers.length-1;
        while(start<end){
            if(numbers[end]+numbers[start]>target){
                end--;
            }else if(numbers[end]+numbers[start]<target){
                start++;
            }else{
                if(start!=end){
                    return new int[]{start+1,end+1};

                }
                
            }
        }
        return new int[]{};
        
    }
}
