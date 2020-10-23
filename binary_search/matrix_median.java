import java.util.Collections;
public class Solution {
    public int findMedian(ArrayList<ArrayList<Integer>> A) {
        int med = 0;
        int N = A.size();
        int M = A.get(0).size();
        int mid = (N*M)/2;
        med = getSortedArray(A).get(mid);
        return med;
    }
    
    private ArrayList<Integer> getSortedArray(ArrayList<ArrayList<Integer>> A){
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(ArrayList<Integer> AI : A){
            arr.addAll(AI);
        }
        
        Collections.sort(arr);
        return arr;
    }
}
