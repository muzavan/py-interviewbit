class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        res = []
        for e in range(1,A+1):
            if e%15 == 0:
                res.append("FizzBuzz")
            elif e%5 == 0:
                res.append("Buzz")
            elif e%3 == 0:
                res.append("Fizz")
            else:
                res.append("{0}".format(e))
                
        return res
