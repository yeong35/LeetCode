class Solution {
    public int passThePillow(int n, int time) {
        int num = 1;
        boolean turn = false;
        for(int i = 0; i < time; i++){
            if(!turn)
                num++;
            else
                num--;

            if(num>n){
                num = n-1;
                turn = true;
            }
            else if(num < 1){
                num = 2;
                turn = false;
            }
        }

        return num;
    }
}