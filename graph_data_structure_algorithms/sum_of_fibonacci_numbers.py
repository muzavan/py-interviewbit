class Solution:
	# @param A : integer
	# @return an integer
	def fibsum(self, A):
	    if A <= 0:
	        return 0
	        
	    fib = [1, 2]
	    prev, curr = 1, 2
	    
	    # Populate the possible fibbonaci list
	    while curr < A:
	        tmp = curr
	        curr = curr + prev
	        prev = tmp
	        
	        fib.append(curr)
	        
	    fib.reverse()
	    return self.get_min(A, fib)
	
	
	def get_min(self, A, fib):
	    # fib sorted DESC
	    if A <= 0:
	        return 0
	        
	    # We find the closest fib numbers to the target
	    # Using greedy
	    # Note: probably can find the required element better by using binary search?
	    for i, f in enumerate(fib):
	        if f <= A:
	            break
	         
	    return 1 + self.get_min(A - f, fib[i+1:])
	    