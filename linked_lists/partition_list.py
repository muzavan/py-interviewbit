# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        less = None
        more = None
        K = A
        headLess = None
        headMore = None
        while K:
            val = K.val
            nxt = K.next
            
            K.next = None
            if val < B:
                if not headLess:
                    headLess = K
                    less = K
                else:
                    less.next = K
                    less = K
            else:
                if not headMore:
                    headMore = K
                    more = K
                else:
                    more.next = K
                    more = K
                
            K = nxt
        
        head = headMore
        if headLess:
            head = headLess
            less = headLess
            while less.next:
                less = less.next
                
            less.next = headMore
            
        return head
        
    def addToLess(self, less, newA):
        dless = less
        while less and less.next:
            less = less.next
        
        if not less:
            dless = newA
        else:
            less.next = newA
        
        return dless
        
    def addToMore(self, more, newA):
        return self.addToLess(more, newA)
        
    def printList(self, L):
        Ls = []
        while L:
            Ls.append("{}".format(L.val))
            L = L.next
            
            
        print(" ->".join(Ls))
        
            
