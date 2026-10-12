class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        //the target indices will be at most target, after being sorted
        //could this be done with two pointers?
        //count how many numbers are smaller than target
        int numsLessThanTarget = 0;
        int numsEqualToTarget = 0;
        List<Integer> ansArray = new ArrayList<>();
        for (int i = 0; i < nums.length; i++){
            if (nums[i] < target){
                numsLessThanTarget += 1;
            }
            if (nums[i] == target){
                numsEqualToTarget += 1;
            }
        }
        // FIX: Moved outside the counting loop — build ansArray once after counting is complete
        for (int j = 0; j < numsEqualToTarget; j++){
            ansArray.add(numsLessThanTarget + j); // FIX: offset j by numsLessThanTarget to get the actual sorted index
        }
        return ansArray;
    }
}