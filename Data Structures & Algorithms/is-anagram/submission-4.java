class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> freq = new HashMap<>();

        for (char c: s.toCharArray()){
            if (freq.containsKey(c)) {
                freq.put(c, freq.get(c) + 1);
            } else {
                freq.put(c, 1);
            }
        }

        for (char c: t.toCharArray()){
             if (!freq.containsKey(c) || freq.get(c) <= 0) {
                return false;
            } else {
                freq.put(c, freq.get(c) - 1);
            }
        }

        return true;



    }
}
