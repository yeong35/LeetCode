class Solution {

    public int numIslands(char[][] grid) {
        
        int cnt = 0;

        int m = grid.length;        // row
        int n = grid[0].length;     // column

        int[][] checker = new int[m][n];
        int row, col;

        Queue<Integer> que_row = new LinkedList<>();
        Queue<Integer> que_col = new LinkedList<>();

        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                if(checker[i][j] != 1 && grid[i][j] != '0'){
                    
                    cnt++;
                    checker[i][j] = 1;

                    // add all direction
                    addDirection(que_row, que_col, i, j);

                    while(!que_row.isEmpty()){
                        row = que_row.poll();
                        col = que_col.poll();

                        if(!outOfEdge(row, m) && !outOfEdge(col, n) && checker[row][col] == 0 && grid[row][col]=='1'){
                            checker[row][col] = 1;
                            addDirection(que_row, que_col, row, col);
                        }
                    }
                }
            }
        }

        return cnt;
    }

    private void addDirection(Queue<Integer> que_row, Queue<Integer> que_col, int i, int j){

        que_row.add(i-1);
        que_col.add(j);

        que_row.add(i+1);
        que_col.add(j);

        que_row.add(i);
        que_col.add(j-1);

        que_row.add(i);
        que_col.add(j+1);
    }

    private boolean outOfEdge(int target, int length){
        if(target < 0 || target >= length)
            return true;
        
        else
            return false;

    }
}