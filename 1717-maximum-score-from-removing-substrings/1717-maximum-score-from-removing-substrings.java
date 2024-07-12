class Solution {
    public int maximumGain(String s, int x, int y) {
        StringBuilder sb = new StringBuilder(s);
        Stack<Integer> stack = new Stack<>();
        int idx = 0;
        int result = 0;

        if(x>y){
            for(int i = 0; i<sb.length(); i++){
                if(sb.charAt(i) != 'a' && sb.charAt(i) !='b')
                    stack.clear();
                else if(sb.charAt(i)=='a')
                    stack.push(i);
                else if(sb.charAt(i)=='b' && !stack.isEmpty()){
                    sb.delete(stack.pop(), i+1);
                    i-=2;
                    result += x;
                }
            }
            stack.clear();
            for(int i = 0; i<sb.length(); i++){
                if(sb.charAt(i) != 'a' && sb.charAt(i) !='b')
                    stack.clear();
                else if(sb.charAt(i)=='b')
                    stack.push(i);
                else if(sb.charAt(i)=='a' && !stack.isEmpty()){
                    sb.delete(stack.pop(), i+1);
                    i-=2;
                    result += y;
                }
            }

        }
        else{
            for(int i = 0; i<sb.length(); i++){
                
                if(sb.charAt(i) != 'a' && sb.charAt(i) !='b')
                    stack.clear();
                else if(sb.charAt(i)=='b')
                    stack.push(i);
                else if(sb.charAt(i)=='a' && !stack.isEmpty()){
                    sb.delete(stack.pop(), i+1);
                    i-=2;
                    result += y;
                }
            }
            stack.clear();
            for(int i = 0; i<sb.length(); i++){
                if(sb.charAt(i) != 'a' && sb.charAt(i) !='b')
                    stack.clear();
                else if(sb.charAt(i)=='a')
                    stack.push(i);
                else if(sb.charAt(i)=='b' && !stack.isEmpty()){
                    sb.delete(stack.pop(), i+1);
                    i-=2;
                    result += x;
                }
            }
        }

        return result;

    }
}