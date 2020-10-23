public class Solution {
    public ArrayList<ArrayList<Integer>> solve(int A, ArrayList<ArrayList<Integer>> B) {
        int rowLen = B.size();
        int colLen = B.get(0).size();
        
        int[][][] curr = new int[A+1][rowLen][colLen];
        
        for(int i=0; i < rowLen; i++){
            for(int j=0; j < colLen; j++){
                curr[0][i][j] = B.get(i).get(j);
            }
        }
        
        
        for(int k=1; k <= A; k++){
            int[][] prev = curr[k-1];
            
            for(int i=0; i < rowLen; i++){
                for(int j=0; j < colLen; j++){
                    int[] poss = getPoss(i, j, rowLen, colLen, prev);
                    curr[k][i][j] = getMax(poss);
                }
            }
        }
        
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        
        for(int i=0; i < rowLen; i++){
            ArrayList<Integer> s = new ArrayList<Integer>();
            for(int j=0; j < colLen; j++){
                s.add(new Integer(curr[A][i][j]));
            }
            
            res.add(s);
        }
        return res;
    }
    
    
    public int getMax(int[] arrs){
        int mx = 0;
        
        for(int a : arrs){
            if (a > mx){
                mx = a;
            }
        }
        
        return mx;
    }
    
    public int[] getPoss(int i, int j, int rowLen, int colLen, int[][] dp){
        int[] poss = new int[5];
        
        if (i-1 >= 0){
            poss[0] = dp[i-1][j];
        }
        
        if (j-1 >= 0){
            poss[1] = dp[i][j-1];
        }
        
        if (i+1 < rowLen){
            poss[2] = dp[i+1][j];
        }
        
        if (j+1 < colLen){
            poss[3] = dp[i][j+1];
        }
        
        poss[4] = dp[i][j];
        
        
        return poss;
        
        
    }
}
