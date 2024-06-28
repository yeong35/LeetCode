class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();

        int sum = 0;
        int temp = 0;

        int i = a.length()-1;
        int j = b.length()-1;

        while(i > -1 || j > -1){
            sum = temp;
            if(i > -1){
                sum += a.charAt(i) - '0';
                i--;
            }

            if(j > -1){
                sum += b.charAt(j) - '0';
                j--;
            }

            sb.append(sum%2);
            temp = sum/2;

        }

        if(temp > 0){
            sb.append(temp);
        }

        return sb.reverse().toString();
        
    }
}