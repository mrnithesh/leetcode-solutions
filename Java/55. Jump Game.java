class Solution {
    public boolean canJump(int[] nums) {
        int goal = nums.length-1;
        for (int i=nums.length-2;i>=0;i--){
            if (i+nums[i]>=goal){
                goal = i;
            }
        }
        return goal ==0;
    }
}

//another approach

class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length<=1){
            return true;
        }
        int maxReach=0;
        for (int i=0;i<nums.length;i++){
            if (i>maxReach){
                return false;
            }
            maxReach = Math.max(maxReach,i+nums[i]);
            if (maxReach >= nums.length-1){
                return true;
            }
        }
        return maxReach >= nums.length-1;
    }
}