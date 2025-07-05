class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int res = Integer.MAX_VALUE;
        int start = 0;
        int windowsum = 0;
        for (int end = 0;end <nums.length;end++){
            windowsum = windowsum + nums[end];

            while (windowsum >= target){
                res = Math.min(res, end-start+1);
                windowsum = windowsum - nums[start];
                start = start + 1;
            }

        }
        if (res==Integer.MAX_VALUE){
            return 0;
        }
        else{
            return res;
        }
    }
}