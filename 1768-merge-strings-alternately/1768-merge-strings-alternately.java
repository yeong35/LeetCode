class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();

        int idx = 0;

        while(idx < word1.length() || idx < word2.length()){
            if(idx<word1.length())
                sb.append(word1.charAt(idx));
            
            if(idx<word2.length())
                sb.append(word2.charAt(idx));
            
            idx++;
        }
        
        return sb.toString();
    }
}