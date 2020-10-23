public class Solution {
    // DO NOT MODFIY THE LIST. 
    
    public int maxSubArray(final List<Integer> a){
        if(isAllNotPositive(a)){
            // If no positive number, the max should be 0 or the maximum negative
            return findMaximum(a);
        }
        
        int max = 0;
        int sum = 0;
        for(int i=0; i < a.size(); i++){
            sum += a.get(i);
            max = max(max,sum);
            if(sum < 0){
                sum = 0;
            }
        }
        
        return max;
    }
    
    public int findMaximum(List<Integer> A){
        int max = Integer.MIN_VALUE;
        
        for(int x : A){
            if(x > max){
                max = x;
            }
        }
        
        return max;
    }
    
    public boolean isAllNotPositive(List<Integer> A){
        return A.stream().noneMatch((x) -> (x > 0));
    }
    
    public int max(int a, int b){
        return a > b ? a : b;
    }
}
