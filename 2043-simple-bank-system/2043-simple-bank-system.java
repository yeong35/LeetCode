class Bank {
    long[] accounts = null;
    public Bank(long[] balance) {
        accounts = balance;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if(account1<=accounts.length && account2<=accounts.length && accounts[account1-1]>= money){
            withdraw(account1, money);
            deposit(account2, money);
            return true;
        }
        else
            return false;
    }
    
    public boolean deposit(int account, long money) {
        if(account <= accounts.length){
            accounts[account-1]+=money;
            return true;
        }
        else
            return false;
    }
    
    public boolean withdraw(int account, long money) {
        if(account <= accounts.length && accounts[account-1] >= money){
            accounts[account-1]-=money;
            return true;
        }
        else
            return false;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */