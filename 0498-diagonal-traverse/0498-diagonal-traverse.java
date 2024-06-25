class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int i = 0;
        int j = 0;

        int m = mat.length;
        int n = mat[0].length;

        int[] result = new int[m * n];
        int index = 0;

        boolean increase = true;

        while (index < m*n) {

            System.out.println(i + " " + j + " " + index);
            result[index] = mat[i][j];
            index++;

            if (increase) {
                i--;
                j++;
                
                // 대각선
                if(i < 0 && j >= n){
                    i += 2;
                    j = n-1;

                    increase = false;
                }
                // 위
                else if(i < 0){
                    i = 0;

                    increase = false;
                }
                // 오른쪽
                else if(j >= n){
                    j = n-1;
                    i += 2;

                    increase = false;
                }
            } else {
                i++;
                j--;

                // 대각선
                if(i >= m && j < 0){
                    i = m-1;
                    j += 2;

                    increase = true;
                }
                // 아래
                else if(i >= m){
                    i = m-1;
                    j += 2;

                    increase = true;
                }
                // 왼쪽
                else if(j < 0){
                    j = 0;

                    increase = true;
                }
            }
        }

        return result;
    }

    public boolean outofindex(int i, int j, int m, int n) {
        if (i < 0 || j < 0 || i >= m || j >= n)
            return true;

        return false;
    }
}