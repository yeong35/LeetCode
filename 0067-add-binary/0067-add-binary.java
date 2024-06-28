class Solution {
    public String addBinary(String a, String b) {
        int m = 0;
        int n = 0;

        for(int i = a.length()-1, temp = 1; i>-1; i--, temp*=2){
            m += temp * (a.charAt(i)-48);
        }

        for(int i = b.length()-1, temp = 1; i>-1; i--, temp*=2){
            n += temp * (b.charAt(i) - 48);
        }

        int sum = m+n;

        if(sum==0)
            return "0";

        StringBuilder result = new StringBuilder();

        while(sum > 0){
            result.append(sum%2);
            sum /= 2;
        }

        return result.reverse().toString();
    }
}