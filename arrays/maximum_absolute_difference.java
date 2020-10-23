public class Solution {
    public int maxArr(ArrayList<Integer> A) {
        int max1 = Integer.MIN_VALUE;
        int max2 = Integer.MIN_VALUE;
        int max3 = Integer.MIN_VALUE;
        int max4 = Integer.MIN_VALUE;
        int max = Integer.MIN_VALUE;
        
        for(int i=0; i < A.size(); i++){
            max1 = max(max1, A.get(i)+i);
            max2 = max(max2, A.get(i)-i);
            max3 = max(max3, -A.get(i)+i);
            max4 = max(max4, -A.get(i)-i);
        }
        
        for(int i=0; i < A.size(); i++){
            max = max(max, max1-A.get(i)-i);
            max = max(max, max2-A.get(i)+i);
            max = max(max, max3+A.get(i)-i);
            max = max(max, max4+A.get(i)+i);
        }
        
        return max;
    }
    
    public int max(int a , int b){
        return a > b ? a : b;
    }
}
