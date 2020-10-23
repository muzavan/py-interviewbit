public class Solution {
    // X and Y co-ordinates of the points in order.
    // Each point is represented by (X.get(i), Y.get(i))
    public int coverPoints(ArrayList<Integer> X, ArrayList<Integer> Y) {
        int size = X.size() == Y.size() ? X.size() : 0;
        if(size <= 1){
            return 0;
        }

        int prevX = X.get(0), prevY = Y.get(0);
        int minStep = 0;

        for(int i=1; i < size; i++){
            int stepX = X.get(i) - prevX;
            int stepY = Y.get(i) - prevY;

            stepX = (stepX < 0) ? -1*stepX : stepX;
            stepY = (stepY < 0) ? -1*stepY : stepY;

            minStep = minStep + (stepX > stepY ? stepX : stepY);
            prevX = X.get(i);
            prevY = Y.get(i);
        }

        return minStep;
    }
}
