class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        boolean res = false;
        int n = nums.size();

        for (int i= 0;i<=n-2*k;i++){
            boolean first = true;
            boolean second = true;
            for (int a =i;a<i+k-1;a++){
                if (nums.get(a)>=nums.get(a+1)){
                    first = false;
                    break;
                }
            }
            if (!first){
                continue;
            }
            for (int b =i+k;b<i+2*k-1;b++){
                if (nums.get(b)>=nums.get(b+1)){
                    second = false;
                    break;
                }
            }
            if (first && second){
                res = true;
                return res;
            }
        }
        return res;
    }
}