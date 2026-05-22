class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        HashMap<Character,Integer>map1=new HashMap<Character,Integer>();
        int currentcount=0;
        for(int i=0;i<s.length();i++){
            if(map1.containsKey(s.charAt(i))){
                currentcount=map1.get(s.charAt(i));
                map1.put(s.charAt(i),currentcount+1);
            }else{
                map1.put(s.charAt(i),0);
            }
        }
        HashMap<Character,Integer>map2=new HashMap<Character,Integer>();
        for(int i=0;i<t.length();i++){
            if(map2.containsKey(t.charAt(i))){
                currentcount=map2.get(t.charAt(i));
                map2.put(t.charAt(i),currentcount+1);
            }else{
                map2.put(t.charAt(i),0);
            }
        }
        if(map1.equals(map2)){
            return true;
        }
        return false;
    }
}
