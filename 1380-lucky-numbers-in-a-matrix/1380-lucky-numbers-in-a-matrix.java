class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        List<Integer> nums = new LinkedList<>();
        int temp;
        int col;
        boolean lucky;

        int m = matrix.length;
        int n = matrix[0].length;

        for(int i = 0; i<m; i++){
            temp = matrix[i][0];
            col = 0;
            lucky = true;

            for(int j = 0; j<n; j++){
                if(temp > matrix[i][j]){
                    temp = matrix[i][j];
                    col = j;
                }
            }

            for(int j = 0; j<m; j++){
                if(temp < matrix[j][col])
                    lucky = false;
            }

            if(lucky)
                nums.add(matrix[i][col]);
        }

        return nums;

    }
}