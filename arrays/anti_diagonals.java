public class Solution {
    public ArrayList<ArrayList<Integer>> diagonal(ArrayList<ArrayList<Integer>> a) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>(); 
        if(a.size() != 0){
           int size = a.size();
           for(int i=0; i <= 2*(size-1);i++){
               result.add(getDiagonalFromSum(a,i));
           }
        }
        return result;
    }
    
    private ArrayList<Integer> getDiagonalFromSum(ArrayList<ArrayList<Integer>> a, int n){
        ArrayList<Integer> ints = new ArrayList<Integer>();
        int size = a.size();
        for(int i=0; i<=n;i++){
            if(i >= size || (n-i) >= size){
                continue;
            }
            ints.add(a.get(i).get(n-i));
        }
        return ints;
    }
}
