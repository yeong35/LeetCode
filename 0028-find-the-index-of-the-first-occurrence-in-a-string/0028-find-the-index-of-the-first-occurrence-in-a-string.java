class Solution {
    public int strStr(String haystack, String needle) {

        boolean find = true;

        for(int i = 0; i<haystack.length(); i++){
            find = true;

            for(int j = 0; j<needle.length(); j++){
                if(i+j >= haystack.length() ||haystack.charAt(i+j) != needle.charAt(j)){
                    find = false;
                    break;
                }
            }

            if(find)
                return i;
        }

        return -1;
    }
}