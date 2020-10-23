import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
public class Solution {
    // DO NOT MODIFY THE LIST
    public ArrayList<Integer> repeatedNumber(final List<Integer> a) {
            ArrayList<Integer> dm = new ArrayList<Integer>();
            Remainder rm = getRemainder(a);
            long plus = rm.square / rm.normal;
            long missing = (plus - rm.normal) / 2;
            long duplicate = plus - missing;
            
            dm.add((int)duplicate);
            dm.add((int)missing);
            return dm;
    }
        
        private Remainder getRemainder(final List<Integer> a){
            Remainder rm = new Remainder();
            BigInteger actSum = BigInteger.valueOf(0);
            BigInteger sum = BigInteger.valueOf(0);
            BigInteger actSquareSum = BigInteger.valueOf(0);
            BigInteger squareSum = BigInteger.valueOf(0);
            
            for(int i=0; i<a.size(); i++){
                BigInteger num = BigInteger.valueOf(a.get(i));
                
                sum = sum.add(num);
                squareSum = squareSum.add(num.multiply(num));
                
                // actual result
                BigInteger j = BigInteger.valueOf(i+1);
                actSum  = actSum.add(j);
                actSquareSum = actSquareSum.add(j.multiply(j));                
            }
            
            rm.normal = Long.valueOf(String.valueOf(sum.subtract(actSum)));
            rm.square = Long.valueOf(String.valueOf(squareSum.subtract(actSquareSum)));
            return rm;
        }
        
        private class Remainder{
            public long normal;
            public long square;
        }
}
