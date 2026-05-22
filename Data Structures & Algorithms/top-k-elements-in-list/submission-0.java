class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer>map=new HashMap<Integer,Integer>();
        int l=nums.length;
        List<List<Integer>>result=new ArrayList<>(l+1);
        for (int i = 0; i <= l; i++) {
            result.add(new ArrayList<>());
        }
        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int frequency = entry.getValue();
            int number = entry.getKey();
            result.get(frequency).add(number);
        }
        int answer[]=new int[k];
        int count=0;
        for(int i=l;i>=1;i--){
            for(int num: result.get(i)){
                if(count<k){
                    answer[count++]=num;
                }else{
                    return answer;
                }
            }

        }
        return answer;
    }
}
