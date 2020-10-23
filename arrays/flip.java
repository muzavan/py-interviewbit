public class Solution {
    public ArrayList<Integer> flip(String A) {
        ArrayList<Integer> flips = new ArrayList<>();
        // Idea: using modified version of Kadane Algorithm
        int maxAddedNum = 0;
        int maxLeft = -1;
        int maxRight= -1;
        int i=0;
        char c;
        while(i < A.length()){            
            c = A.charAt(i);
            if(c == '0'){
                break;
            }
            i++;
        }
        
        while(i < A.length()){
            int count = 0;
            int left = i;
            while(count >= 0 && i < A.length()){
                c = A.charAt(i);
                if(c == '0'){
                   count++;
                }
                else{
                   count--; 
                }
                if(count > maxAddedNum){
                    maxAddedNum = count;
                    maxLeft = left;
                    maxRight = i;
                }
                i++;
            }            
        }
        
        if(maxLeft != -1){
            flips.add(maxLeft+1);
            flips.add(maxRight+1);
        }
        
        return flips;
    }
}
