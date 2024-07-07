class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int emptyBottles = numBottles;
        int result = numBottles;

        while(emptyBottles >= numExchange){
            numBottles = emptyBottles/numExchange;
            emptyBottles = emptyBottles%numExchange + numBottles;

            result += numBottles;
        }

        return result;

    }
}