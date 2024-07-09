class Solution {
    public double averageWaitingTime(int[][] customers) {
        int time = customers[0][0];
        double sum = 0;
        int prev_order = customers[0][0];

        for(int i = 0; i<customers.length; i++){
            time = customers[i][0];
            if(prev_order > time){
                prev_order = prev_order+customers[i][1];
                sum += prev_order - time;
            }
            else{
                prev_order = time + customers[i][1];
                sum += customers[i][1];
            }
        }

        return sum / customers.length;
    }
}