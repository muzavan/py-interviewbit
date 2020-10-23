public class Solution {
    public ArrayList<Integer> plusOne(ArrayList<Integer> a) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        ArrayList<Integer> tresult = new ArrayList<Integer>();
        boolean skip = true;
        for(int i=0; i < a.size(); i++){
            if(a.get(i) == 0 && skip && a.size() != 1){
                continue;
            }
            skip = false;
            tresult.add(a.get(i));
        }

        int last = tresult.get(tresult.size()-1) + 1;
        boolean carry = last > 9;
        tresult.set(tresult.size()-1,last%10);

        for(int i=tresult.size()-2; i >=0; i--){
            int tlast = carry ? tresult.get(i) + 1 : tresult.get(i);
            carry = tlast > 9;
            tresult.set(i, tlast%10);
        }
        if(carry){
            result.add(1);
            result.addAll(tresult);
        }
        else{
            result.addAll(tresult);
        }

        return result;
    }
}
