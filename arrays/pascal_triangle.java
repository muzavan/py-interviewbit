public class Solution {
    public ArrayList<ArrayList<Integer>> generate(int a) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        for(int i=0; i<a; i++){
            if(i == 0){
                result.add(getArrayList(new ArrayList<Integer>()));
            }
            else{ 
                result.add(getArrayList(result.get(result.size()-1)));   
            }
        }
        return result;
    }
    
    private ArrayList<Integer> getArrayList(ArrayList<Integer> base){
        ArrayList<Integer> ints = new ArrayList<Integer>();
        if(base.size() == 0){
            ints.add(1);
        }
        else{
            ints.add(1);
            for(int i=0; i < base.size()-1;i++){
                ints.add(base.get(i)+base.get(i+1));
            }
            ints.add(1);
        }
        
        return ints;
    }
}
