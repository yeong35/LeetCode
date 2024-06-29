class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder sb = new StringBuilder();
        char temp;
        for(int i = 0; i < 200; i++){
            temp = '0';
            for(int j = 0; j<strs.length; j++){
                if(strs[j].length() <= i)
                    return sb.toString();

                if(temp == '0')
                    temp = strs[j].charAt(i);
                else if(temp != strs[j].charAt(i))
                    return sb.toString();
            }

            sb.append(strs[0].charAt(i));
        }

        return sb.toString();

    }
}