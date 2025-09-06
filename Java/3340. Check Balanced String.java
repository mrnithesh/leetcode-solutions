class Solution {
    public boolean isBalanced(String num) {
        int ans=0;
        for(int i=0;i<num.length();i++){
            if(i%2==0){
                ans+=num.charAt(i)-'0';
            }
            else{
                ans-=num.charAt(i)-'0';
            }
        }
        return ans==0;
    }
}