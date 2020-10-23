class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        ln = 0
        s = set()
        mx = 0
        for a in A:
            print(s)
            if a not in s:
                ln += 1
                s.add(a)
            else:
                if ln > mx:
                    mx = ln
                ln = 1
                s = set()
                s.add(a)
        
        if ln > mx:
            mx = ln
        return mx
