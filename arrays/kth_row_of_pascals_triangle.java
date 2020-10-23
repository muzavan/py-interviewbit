public class Solution {
    public ArrayList<Integer> getRow(int a) {
        ArrayList<Integer> row = new ArrayList<Integer>();
        for(int i=0; i<=a; i++){
            row = getArrayList(row);
        }
        
        return row;
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
