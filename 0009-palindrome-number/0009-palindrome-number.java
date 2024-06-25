class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0)
            return false;
        
        String s = Integer.toString(x);
        int length = s.length();

        for(int i = 0; i<length/2; i++){
            if(s.charAt(i) != s.charAt(length-1-i))
                return false;
        }

        return true;
    }
}