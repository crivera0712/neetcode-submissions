class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> dupe = new HashSet<Integer>();
        for (int n: nums){
            if (dupe.contains(n)){
                return true; 
            }
            dupe.add(n);
        }
        return false; 


    }
}
