#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:

    # @param A : string
    # @param B : string
    # @return a strings

    def minWindow(self, A, B):
        cnt = {}
        
        for b in B:
            if b not in cnt:
                cnt[b] = 0
            cnt[b] += 1

        si, ei = 0, 0
        dcnt = {}
        mn = ''
        while ei < len(A):
            a = A[ei]
            if a not in dcnt:
                dcnt[a] = 0
                
            dcnt[a] += 1
            
            check = False
            s = None
            while self.isValid(cnt, dcnt, s):
                # Find maximum si
                check = True
                s = A[si]
                dcnt[s] -= 1
                si += 1
            
            if check:    
                smn = A[si-1:ei+1]
                if len(smn) < len(mn) or mn == '':
                    mn = smn
                
            ei += 1
                
        return mn

    def isValid(self, cnt, dcnt, a = None):
        if a and a in cnt:
            if dcnt[a] < cnt[a]:
                return False
            return True
        for c in cnt.keys():
            if c not in dcnt or cnt[c] > dcnt[c]:
                return False

        return True



            