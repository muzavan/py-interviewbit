# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def separate(self, A, k):
        nA = 0
        dummy = ListNode(0)
        dummy.next = A
        K = dummy
        prev = None
        while nA <= k-1:
            nA += 1
            prev = K
            K = K.next
            
        prev.next = K.next
        K.next = None
        
        return dummy.next, K
        
    def sortList(self, A):
        if not A or not A.next:
            return A

        nA = 0
        K = A
        
        while K:
            nA += 1
            K = K.next
            
        mid = nA/2
        A, Amid = self.separate(A, mid)
        self.printList(A)
        self.printList(Amid)
        
        A = self.partition(A, Amid)
        return A
        
    def partition(self, A, KB):
        B = KB.val
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
        
        self.printList(headLess)
        self.printList(headMore)
        
        if headMore:
            headMore = self.sortList(headMore)
            KB.next = headMore
            head = KB
    
        if headLess:
            headLess = self.sortList(headLess)
            head = headLess
            less = headLess
            while less.next:
                less = less.next
                
            less.next = KB
            
        return head
        
    def printList(self, L):
        return None
        Ls = []
        while L:
            Ls.append("{}".format(L.val))
            L = L.next
            
            
        print(" ->".join(Ls))
    
            
