class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false; 
        }

        HashMap <Character, Integer> check = new HashMap<>();
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        for (int i = 0; i < sArray.length; i++){
            char charSHolder = sArray[i];
            char charTHolder = tArray[i];

            if (check.containsKey(charSHolder)){
                check.put(charSHolder, check.get(charSHolder) + 1);
            } else {
                check.put(charSHolder, 1);
            }
            if (check.containsKey(charTHolder)){
                check.put(charTHolder, check.get(charTHolder) - 1);
            } else {
                check.put(charTHolder, -1);
            }
        }
    
    for (Integer value : check.values()){
        System.out.println(value);
        if (value != 0){
            return false; 
        }
    }
    
    return true; 

    }
}
