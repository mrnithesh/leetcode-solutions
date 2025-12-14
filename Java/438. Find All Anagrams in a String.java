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
//faster and better approach using prefix sum
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();

        if (s.length() < p.length()) {
            return res;
        }

        int[] freqP = new int[26];
        int[] freqWindow = new int[26];

        for (char c : p.toCharArray()) {
            freqP[c - 'a']++;
        }

        int windowSize = p.length();

        for (int i = 0; i < windowSize; i++) {
            freqWindow[s.charAt(i) - 'a']++;
        }

        if (Arrays.equals(freqP, freqWindow)) {
            res.add(0);
        }

        for (int i = windowSize; i < s.length(); i++) {
            freqWindow[s.charAt(i) - 'a']++;
            freqWindow[s.charAt(i - windowSize) - 'a']--;
            if (Arrays.equals(freqP, freqWindow)) {
                res.add(i - windowSize + 1);
            }
        }

        return res;
    }
}
