class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int currentsum = 0;
        for (int i=0;i<k;i++){
            currentsum = currentsum + nums[i];
        }
        double maxavg = (double)currentsum/k;
        for (int i=k;i<nums.length;i++){
            currentsum = currentsum + nums[i]- nums[i-k];
            maxavg = Math.max(maxavg,(double) currentsum/k);
        }
        return maxavg;
    }
}