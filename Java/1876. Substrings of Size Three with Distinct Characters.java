class Solution {
    public int countGoodSubstrings(String s) {
        int res = 0, i =0, j =3;
        while(j<=s.length()){
            String window = s.substring(i,j);
            Set<Character> set = new  HashSet<>();
            for (char ch : window.toCharArray()){
                set.add(ch);
            }
            if (set.size() == 3){
                res++;
            }
            i++;
            j++;
        }
        return res;
    }
}