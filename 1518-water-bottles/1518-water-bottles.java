class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int emptyBottles = numBottles;
        int result = numBottles;

        while(emptyBottles/numExchange != 0){
            result += emptyBottles/numExchange;
            emptyBottles = (emptyBottles+emptyBottles/numExchange) / numExchange;
        }

        System.out.println(result + " " +emptyBottles);

        return result;

    }
}