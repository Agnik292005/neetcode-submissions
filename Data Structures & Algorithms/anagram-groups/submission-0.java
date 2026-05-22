class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>>map=new HashMap<>();
        for(String s:strs){
            int characterCount[]=new int[26];
            char[] StringArray=s.toCharArray();
            for(char c:StringArray){
                characterCount[c-'a']++;
            }
            String count=Arrays.toString(characterCount);
            map.putIfAbsent(count,new ArrayList<String>());
            map.get(count).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
