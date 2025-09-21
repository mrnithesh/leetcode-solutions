class Solution {
    int[] dp;
    public int coinChange(int[] coins, int amount) {
        dp= new int[amount+1];
        Arrays.fill(dp,-1);
        int res = solve(coins,amount);
        return res==Integer.MAX_VALUE ? -1:res;
    }
    private int solve(int[] coins,int remAmount){
        if(remAmount==0){
            return 0;
        }
        if (remAmount<0){
            return Integer.MAX_VALUE;
        }
        if(dp[remAmount]!=-1){
            return dp[remAmount];
        }
        int minCoins = Integer.MAX_VALUE;
        for(int coin:coins){
            int res=solve(coins,remAmount-coin);
            if (res!=Integer.MAX_VALUE){
                minCoins= Math.min(minCoins,1+res);
            }
        }
        dp[remAmount] = minCoins;
        return dp[remAmount];
    }
}