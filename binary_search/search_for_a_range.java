public class Solution {
    // DO NOT MODIFY THE LIST
    public ArrayList<Integer> searchRange(final List<Integer> a, int b) {
        // Idea, find the b first. Then find the leftest and rightest index for b
        ArrayList<Integer> result = new ArrayList<Integer>();
        if(a.size() == 0){
            result.add(-1);
            result.add(-1);
            return result;
        }
        
        int checkedIdx = mSearch(a, b, 0, a.size()-1);
        if(checkedIdx == -1){
            result.add(-1);
            result.add(-1);
            return result;
        }
        
        int leftIdx = mSearchLeft(a, b, 0, checkedIdx);
        int rightIdx = mSearchRight(a, b, checkedIdx, a.size()-1);
        
        result.add(leftIdx);
        result.add(rightIdx);
        
        return result;
        
    }
    
    private int mSearch(final List<Integer> a, int b, int startIdx, int endIdx){
        if (startIdx > endIdx){
            return -1;
        }
        
        int checkedIdx = (startIdx+endIdx)/2;
        if(a.get(checkedIdx) > b){
            // SearchLeft
            return mSearch(a, b, startIdx, checkedIdx-1);
        }
        else if (a.get(checkedIdx) < b){
            // SearchRight
            return mSearch(a, b, checkedIdx+1, endIdx);
        }
        return checkedIdx;
    }
    
    private int mSearchLeft(final List<Integer> a, int b, int startIdx, int endIdx){
        if (startIdx > endIdx){
            return -1;
        }
        
        int checkedIdx = (startIdx+endIdx)/2;
        if(a.get(checkedIdx) ==  b){
            if(endIdx == startIdx) return checkedIdx;
            int leftIdx = mSearchLeft(a, b, startIdx, checkedIdx-1);
            if(leftIdx == -1){
                return checkedIdx;
            }
            return leftIdx;
        }
            
        return mSearchLeft(a, b, checkedIdx+1, endIdx);
    }
    
    private int mSearchRight(final List<Integer> a, int b, int startIdx, int endIdx){
        if (startIdx > endIdx){
            return -1;
        }
        
        int checkedIdx = (startIdx+endIdx)/2;
        // System.out.println("Checked Index: "+checkedIdx);
        if(a.get(checkedIdx) ==  b){
            if(endIdx == startIdx) return checkedIdx;
            int rightIdx = mSearchRight(a, b, checkedIdx+1, endIdx);
            if(rightIdx == -1){
                return checkedIdx;
            }
            return rightIdx;
        }
            
        return mSearchRight(a, b, startIdx, checkedIdx-1);
    }
}
