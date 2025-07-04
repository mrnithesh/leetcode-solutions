class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder cleaned = new StringBuilder();
        for (char ch : s.toCharArray()){
            if (Character.isLetterOrDigit(ch)){
                cleaned.append(Character.toLowerCase(ch));
            }
        }
        String cleanedStr = cleaned.toString();
        int l = 0;
        int r = cleanedStr.length()-1;
        while (l<=r){
            if (cleanedStr.charAt(l) != cleanedStr.charAt(r)){
                return false;
            }
            l = l+1;
            r = r-1;
        }
        return true;
    }
}