public class Solution {
    public ArrayList<Integer> primes = new ArrayList<Integer>();
        public ArrayList<Integer> primesum(int a) {
            ArrayList<Integer> ints = new ArrayList<Integer>();
            if(a == 4){
                ints.add(2);
                ints.add(2);
                return ints;
            }
            int limit = a/2;
            for(int i = 3; i <= limit; i+=2){
                if(isPrime(i)){
                    int res = a - i;
                    if(isPrime(res)){
                        ints.add(i);
                        ints.add(res);
                        return ints;
                    }
                }
            }
            return ints;
        }
        
        public boolean isPrime(int a){
            int limit = (int) Math.sqrt(a);
            if(primes.contains(a)){
                return true;
            }
            if(a%2 == 0){
                return false;
            }
            for(int i = 3; i <= limit; i+=2){
                if(a%i == 0){
                    return false;
                }
            }
            primes.add(a);
            return true;
        }
}
