class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        int min = 10000;

        for(int i = 0; i<prices.length; i++){
            result = Math.max(result, prices[i]-min);
            
            min = Math.min(min, prices[i]);

            System.out.println(min + " " + result);
        }

        return result;
    }
}