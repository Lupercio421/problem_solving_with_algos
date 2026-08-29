class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> modSeen = new HashMap<>();
        modSeen.put(0,-1);
        int total = 0;

        for (int i = 0; i < nums.length; i++) {
            total = (total + nums[i]) % k;

            if (modSeen.containsKey(total)){
                if (i - modSeen.get(total) > 1){
                    return true;
                }
            } else{
                modSeen.put(total, i);
            }
        }
        return false;
    }
}