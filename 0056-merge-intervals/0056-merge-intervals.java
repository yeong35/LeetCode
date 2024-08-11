class Solution {
    public int[][] merge(int[][] intervals) {
        ArrayList<int[]> temp = new ArrayList<>();

        for(int i = 0; i<intervals.length; i++){
            if(intervals[i][0] == -1)
                continue;

            temp.add(merge(intervals[i][0], intervals[i][1], intervals));
        }

        int[][] result = new int[temp.size()][2];

        for(int i = 0; i<result.length; i++){
            result[i][0] = temp.get(i)[0];
            result[i][1] = temp.get(i)[1];
        }
        
        return result;
    }

    private int[] merge(int start, int end, int[][] intervals){
        
        int m, n;

        for(int i = 0; i<intervals.length; i++){
            m = intervals[i][0];
            n = intervals[i][1];

            if(m >= start && m <= end){
                end = Math.max(n, end);
                intervals[i][0] = -1;
            }
            if(n >= start && n <= end){
                start = Math.min(start, m);
                intervals[i][0] = -1;
            }
        }

        return new int[] {start, end};
    }
}