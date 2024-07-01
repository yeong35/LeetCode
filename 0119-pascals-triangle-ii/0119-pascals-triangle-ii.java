class Solution {
    public List<Integer> getRow(int rowIndex) {

        List<List<Integer>> result = new ArrayList<>();
        List<Integer> prev = null;
        List<Integer> current = null;

        result.add(new ArrayList<Integer>());
        current = result.get(0);
        current.add(1);


        for(int i = 1; i<=rowIndex; i++){
            result.add(new ArrayList<Integer>());
            prev = result.get(i-1);
            current = result.get(i);
            current.add(1);

            for(int j=1; j<i; j++){
                current.add(prev.get(j-1)+prev.get(j));
            }   
            current.add(1);
        }

        return result.get(rowIndex);
    }
}