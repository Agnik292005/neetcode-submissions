class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer>map=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            map.put(nums[i],0);
        }
        for(int i=0;i<nums.length;i++){
            int currentCount=map.get(nums[i]);
            map.put(nums[i],currentCount+1);
            if(map.get(nums[i])>nums.length/2){
                return nums[i];
            }
        }
        return 0;
        
    }
}