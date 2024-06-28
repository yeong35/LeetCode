class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();

        int temp = 0;

        int i = a.length()-1;
        int j = b.length()-1;

        while(i > -1 || j > -1){

            if(i > -1){
                temp += a.charAt(i) - '0';
                i--;
            }

            if(j > -1){
                temp += b.charAt(j) - '0';
                j--;
            }

            sb.append(temp%2);
            temp = temp/2;

        }

        if(temp > 0){
            sb.append(temp);
        }

        return sb.reverse().toString();
        
    }
}