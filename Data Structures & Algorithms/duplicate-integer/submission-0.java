class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer,Integer> unique=new HashMap<Integer, Integer>();
        for(int i=0;i<nums.length;i++){
            unique.put(nums[i],i);
        }
        if(unique.size()==nums.length){
            return false;
        }
        return true;
    }
}