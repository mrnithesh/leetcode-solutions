class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        int res = 0;
        HashSet<Character> set = new HashSet<>();
        for (int r=0;r<s.length();r++){
            char ch = s.charAt(r);
            while (set.contains(ch)){
                set.remove(s.charAt(l));
                l++;
            }
            set.add(s.charAt(r));
            res = Math.max(res,r-l+1);
        }
        return res;
    }
}