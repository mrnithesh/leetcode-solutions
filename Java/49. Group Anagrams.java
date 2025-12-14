class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> res = new HashMap();
        for (String s:strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String temp = new String(chars);
            if (!res.containsKey(temp)){
                res.put(temp, new ArrayList<>());
            }
            res.get(temp).add(s);
        }

        return new ArrayList<>(res.values());
    }
}