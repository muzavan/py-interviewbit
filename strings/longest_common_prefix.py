class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        mx_idx = -1
        mn_len = min([len(a) for a in A])
        
        for i in range(mn_len):
            s_char = set([a[i] for a in A])
            
            all_same = len(s_char) == 1
            
            if not all_same:
                break
            mx_idx = i
        
        if mx_idx == -1:
            return ""
            
        return A[0][:mx_idx+1]
