class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap <Character, Integer> string1 = new HashMap<>(); 
        HashMap <Character, Integer> string2 = new HashMap<>();
 
        for (char c : s.toCharArray()){
            if (string1.containsKey(c)){
                string1.put(c, string1.get(c) + 1);
            } else {
                // char c is not in our HashMap so we must add it
                string1.put(c, 1);
            }
        }

        for (char c : t.toCharArray()){
            if (string2.containsKey(c)){
                string2.put(c, string2.get(c) + 1);
            } else {
                // char c is not in our HashMap so we must add it
                string2.put(c, 1);
            }
        }
        if (string1.equals(string2)){
            return true; 
        }
        return false;
    }
}
