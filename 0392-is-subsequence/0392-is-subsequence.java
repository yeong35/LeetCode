class Solution {
    public boolean isSubsequence(String s, String t) {
        int idx = 0;
        int temp;

        for(int i = 0; i<s.length(); i++){
            temp = t.indexOf(s.charAt(i), idx);
            System.out.println(temp);
            if(temp>-1){
                idx= Math.max(temp+1, idx);
            }
            else{
                return false;
            }
        }

        return true;
    }
}