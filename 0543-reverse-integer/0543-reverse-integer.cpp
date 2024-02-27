class Solution {
public:
    int reverse(int x) {
        unsigned int xx = (unsigned int) (x<0?-x:x);
        unsigned result = 0;
        while(xx>0){
            result = result*10 + xx%10;
            xx/=10;
        }
        return x<0?-result:result;
    }
};