class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        char[] p_chars = p.toCharArray();
        Arrays.sort(p_chars);
        String new_P = new String(p_chars);

        for (int i=0;i<=(s.length()-p.length());i++){
            int j=i+p.length();
            String subString = s.substring(i,j);
            char[] subChars = subString.toCharArray();
            Arrays.sort(subChars);
            String newSubstring = new String(subChars);

            if (newSubstring.equals(new_P)){
                res.add(i);
            }
        }
        return res;
    }
}