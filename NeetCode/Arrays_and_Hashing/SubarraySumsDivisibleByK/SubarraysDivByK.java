class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] map = new int[k];
        map[0] = 1;
        int count = 0, sum = 0;
        for (int num : nums){
            sum = (sum + num) % k;
            if (sum < 0){
                sum += k; //I.e, -1 % 5 = -1
            }
            //Why does the below two lines, inside a else statement, returns a bad answer?
            count += map[sum];
            map[sum]++;
        }
        return count;
    }
}