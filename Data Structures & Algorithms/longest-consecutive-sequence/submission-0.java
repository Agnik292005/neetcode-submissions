class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer>elements=new HashSet<>();
        for(int i=0;i<nums.length;i++){
            elements.add(nums[i]);
        }
        int maxSequence=0;
        for(int i:elements){
            if(!elements.contains(i-1)){
                int count=1;
                while(elements.contains(i+count)){
                    count++;
                }
                maxSequence=Math.max(maxSequence,count);
            }
           
        }
        return maxSequence;
        
    }
}
