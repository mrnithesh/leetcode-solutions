class Solution {
    public String longestPalindrome(String s) {
        String res="";
        int resLen = 0;
        for (int i=0;i<s.length();i++){
            int l=i,r=i;

            while (l>=0 && r<s.length() && s.charAt(l)==s.charAt(r)){
                int currLen = r-l+1;
                if (currLen>resLen){
                    res = s.substring(l,r+1);
                    resLen = currLen;
                }
                r++;
                l--;
            }
            l=i;
            r=i+1;
            while (l>=0 && r<s.length() && s.charAt(l)==s.charAt(r)){
                int currLen = r-l+1;
                if (currLen>resLen){
                    res = s.substring(l,r+1);
                    resLen = currLen;
                }
                r++;
                l--;
            }
        }
        return res;
        
    }
}