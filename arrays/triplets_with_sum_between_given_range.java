public class Solution {
    public int solve(ArrayList<String> A) {
        ArrayList<Double> one = new ArrayList<Double>();
        ArrayList<Double> two = new ArrayList<Double>();
        ArrayList<Double> three = new ArrayList<Double>();
        
        for(int i=0; i < A.size(); i++){
            double d = ToDouble(A.get(i));
            if(d < (2.0/3.0)){
                one.add(d);
                continue;
            }
            if(d < 1){
                two.add(d);
                continue;
            }
            if(d < 2){
                three.add(d);
                continue;
            }
        }
        
        Collections.sort(one);
        Collections.sort(two);
        Collections.sort(three);
        
        // Checking for every case
        // Case AAA
        if(one.size() >= 3){
            int size = one.size();
            double d1 = one.get(size-1);
            double d2 = one.get(size-2);
            double d3 = one.get(size-3);
            
            if((d1+d2+d3) > 1.0){
                return 1;
            }
        }
        
        // Case AAB
        if(one.size()>=2 && two.size() > 0){
            int size = one.size();
            double d1 = one.get(size-1);
            double d2 = one.get(size-2);
            
            double sum = d1+d2;
            for(int i=0; i < two.size();i++){
                if(two.get(i) < (2.0-sum) && two.get(i) > (1.0-sum)){
                    return 1;
                }
            }
        }
        
        // Case ABB
        if(two.size()>=2 && one.size() > 0){
            int size = two.size();
            double d1 = two.get(size-1);
            double d2 = two.get(size-2);
            
            double sum = d1+d2;
            for(int i=0; i < one.size();i++){
                if(one.get(i) < (2.0-sum) && one.get(i) > (1.0-sum)){
                    return 1;
                }
            }
        }
        
        // Case AAC
        if(one.size()>=2 && three.size() > 0){
            double d1 = one.get(0);
            double d2 = one.get(1);
            
            double sum = d1+d2;
            for(int i=0; i < three.size();i++){
                if(three.get(i) < (2.0-sum) && three.get(i) > (1.0-sum)){
                    return 1;
                }
            }
        }
        
        // Case ABC
        if(one.size()>=1 && two.size() >= 1 && three.size() >= 1){
            double d1 = one.get(one.size()-1);
            double d2 = two.get(two.size()-1);
            
            double sum = d1+d2;
            for(int i=0; i < three.size();i++){
                if(three.get(i) < (2.0-sum) && three.get(i) > (1.0-sum)){
                    return 1;
                }
            }
        }
        
        return 0;
    }
    
    private double ToDouble(String s){
        return Double.valueOf(s);
    }
    
}
