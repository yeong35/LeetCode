class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        ArrayList<Integer> result = new ArrayList<>();
        int[][] cnt = new int[2][1001];

        for(int i = 0; i<nums1.length; i++){
            cnt[0][nums1[i]]++;
        }

        for(int i = 0; i<nums2.length; i++){
            cnt[1][nums2[i]]++;
        }

        int temp;
        for(int i = 0; i<1001; i++){
            temp = Math.min(cnt[0][i], cnt[1][i]);
            for(int j = 0; j<temp; j++)
                result.add(i);
        }        
        
        System.out.println(result.size());

        int[] intersection = new int[result.size()];

        for(int i = 0; i<result.size(); i++)
            intersection[i] = result.get(i);

        return intersection;
    }
}