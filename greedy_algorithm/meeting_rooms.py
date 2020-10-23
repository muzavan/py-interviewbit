MAX = 2 * 10**9 + 1

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        en = {}
        st = {}
        
        for a in A:
            tst, ten = a[0], a[1]
            
            if tst not in st:
                st[tst] = 0
                
            if ten not in en:
                en[ten] = 0
                
            st[tst] += 1
            en[ten] += 1
            
        points = set(st.keys()).union(set(en.keys()))
        
        points = sorted(list(points))
        
        mx = 0
        cnt = 0
        for p in points:
            tst = st[p] if p in st else 0
            ten = en[p] if p in en else 0
            
            cnt = cnt + tst - ten
            mx = max(mx, cnt)
            
        return mx
