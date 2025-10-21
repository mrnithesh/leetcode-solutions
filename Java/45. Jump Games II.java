class Solution {
    public int jump(int[] nums) {
        int far = 0;
        int currJump = 0;
        int res = 0;

        for (int i=0;i<nums.length-1;i++){
            far = Math.max(far,i+nums[i]);

            if (i== currJump){
                res++;
                currJump = far;

                if (currJump >= nums.length-1){
                    return res;
                }
            }
        }
        return res;
    }
}