import java.util.Collections;

public class Solution {
    public int solve(ArrayList<Integer> A) {
        ArrayList<Integer> B = A;
        Collections.sort(B);
        int size = B.size();
        for(int i = 0; i < size; i++){
            if(i+1 < size && B.get(i) == B.get(i+1)){
                continue;
            }
            if(B.get(i) == (size-i-1)){
                return 1;
            }
        }
        
        return -1;
    }
}
