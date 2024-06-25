class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();

        int m = matrix.length;
        int n = matrix[0].length;
        int length = m * n;

        int right = 1;
        int down = 1;

        int row = 0;
        int col = -1;

        m--;

        while (result.size() < length) {
            for (int j = 0; j < n; j++) {
                col += right;
                result.add(matrix[row][col]);

                System.out.println(row + " " + col);
            }
            n--;
            right *= -1;

            for (int j = 0; j < m; j++) {
                row += down;
                result.add(matrix[row][col]);
                
                System.out.println(row + " " + col);
            }
            m--;
            down *= -1;
        }

        return result;
    }
}