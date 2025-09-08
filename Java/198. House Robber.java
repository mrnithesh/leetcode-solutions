class Solution {
    private int[] nums;
    private int[] memo;

    public int rob(int[] nums) {
        this.nums = nums;
        memo = new int[nums.length];
        for (int i = 0; i < memo.length; i++) memo[i] = -1; // initialize

        return dp(nums.length - 1);
    }

    private int dp(int i) {
        if (i == 0) return nums[0];
        if (i == 1) return Math.max(nums[0], nums[1]);

        if (memo[i] != -1) return memo[i];

        memo[i] = Math.max(nums[i] + dp(i - 2), dp(i - 1));
        return memo[i];
    }
}
