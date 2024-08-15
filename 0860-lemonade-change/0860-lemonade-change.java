class Solution {
    public boolean lemonadeChange(int[] bills) {
        int[] changes = new int[2];

        for(int i = 0; i<bills.length; i++){
            if(bills[i]==5)
                changes[0]++;
            else if(bills[i]==10){
                if(changes[0]>0){
                    changes[0]--;
                    changes[1]++;
                }
                else
                    return false;
            }
            else{
                if(changes[0]>0 && changes[1]>0){
                    changes[0]--;
                    changes[1]--;
                }
                else if(changes[0]>2)
                    changes[0]-=3;
                else
                    return false;
            }
        }

        return true;
    }
}