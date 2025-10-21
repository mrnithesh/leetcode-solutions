class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int closestSum = nums[0]+nums[1]+nums[2];
        int n = nums.length;
        Arrays.sort(nums);
        for (int i=0;i<n;i++){
            int j = i+1;
            int k= n-1;

            while (j<k){
                int currSum = nums[i]+nums[j]+nums[k];
                int currDiff = Math.abs(currSum-target);
                int closestDiff = Math.abs(closestSum -target);

                if (currDiff<closestDiff){
                    closestSum = currSum;
                }

                if (currSum<target){
                    j++;
                }
                else if (currSum>target){
                    k--;
                }
                else{
                    return currSum;
                }
            }
        }
        return closestSum;
    }
}