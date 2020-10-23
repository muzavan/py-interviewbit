public class Solution {
    public ArrayList<ArrayList<Integer>> generateMatrix(int a) {
        ArrayList<ArrayList<Integer>> mat = new ArrayList<ArrayList<Integer>>();
        int[][] matriks = new int[a][a];
        int direction = 0; // 0 right, 1 down, 2 up, 3 left
        int i=1;
        int max = a*a;
        int curRow = 0;
        int curCol = 0;
        
        while(i <= max){
            int endCol, endRow;
            direction = direction % 4;
            if(direction == 0){
                endCol = a - 1 - curCol;
                while(curCol <= endCol){
                    matriks[curRow][curCol] = i;
                    i++;
                    curCol++;
                }
                curCol = endCol;
                curRow++;
            }
            else if(direction == 1){
                endRow = a - curRow;
                while(curRow <= endRow){
                    matriks[curRow][curCol] = i;
                    i++;
                    curRow++;
                }
                curRow = endRow;
                curCol--;
            }
            else if(direction == 2){
                endCol = a - 2 - curCol;
                while(curCol >= endCol){
                    matriks[curRow][curCol] = i;
                    i++;
                    curCol--;
                }
                curCol = endCol;
                curRow--;
            }
            else if(direction == 3){
                endRow = a - 1 - curRow;
                while(curRow >= endRow){
                    matriks[curRow][curCol] = i;
                    i++;
                    curRow--;
                }
                curRow = endRow;
                curCol++;
            }
            direction++;
        }
        
        for(int k=0; k < a; k++){
            ArrayList<Integer> ints = new ArrayList<>();
            for(int j=0; j < a; j++){
                ints.add(matriks[k][j]);
            }
            mat.add(ints);
        }
        return mat;
    }
}
