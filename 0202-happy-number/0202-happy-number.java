class Solution {
    public boolean isHappy(int n) {
        if(n==1)
            return true;

        HashSet<Integer> set = new HashSet<>();
        int sum=0;

        while(n!=1){
            System.out.println(n);
            if(set.contains(n))
                break;

            set.add(n);

            while(n>0){
                sum += Math.pow(n%10,2);
                n = n/10;
            }

            if(sum==1)
                return true;

            n = sum;
            sum=0;
            
        }
        return false;
    }
}