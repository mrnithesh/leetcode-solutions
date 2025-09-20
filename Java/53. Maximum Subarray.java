class Solution {
    public int maxSubArray(int[] nums) {
        int currSum =0;
        int maxSum = Integer.MIN_VALUE;
        for (int i : nums){
            currSum = Math.max(i, currSum+i);
            maxSum  = Math.max(currSum,maxSum);
        }
        return maxSum;
    }
}