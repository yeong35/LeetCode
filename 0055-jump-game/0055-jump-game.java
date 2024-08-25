class Solution {
    public boolean canJump(int[] nums) {
        
        int goal = nums.length-1;
        int current;
        int[] visited = new int[nums.length];

        Queue<Integer> que = new LinkedList<>();
        que.add(0);
        visited[0] = 1;

        while(!que.isEmpty()){
            current = que.poll();
            System.out.println(current);

            if(current == goal)
                return true;

            for(int i = 1; i<=nums[current]; i++){
                if(current+i <= goal && visited[current+i]==0){
                    que.add(current+i);
                    visited[current+i]=1;
                }
            }
        }

        return false;
    }
}