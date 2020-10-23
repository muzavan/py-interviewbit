# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        dummy = ListNode(0)
        dummy.next = A
        
        prev = dummy
        
        while prev.next:
            tmp = prev
            pmn = prev
            
            while tmp.next:
                if tmp.next.val < pmn.next.val:
                    pmn = tmp
                    
                tmp = tmp.next
                
            # print(pmn.val, tmp.val)
                
            # swap
            it, nextIt = prev.next, prev.next.next
            mn, nextMn = pmn.next, pmn.next.next
            
            #self.printList(it)
            #self.printList(mn)
            
            if nextIt == mn:
                prev.next = mn
                mn.next = it
                it.next = nextMn
            else:
                prev.next = mn
                mn.next = nextIt
                pmn.next = it
                it.next = nextMn
                
            #self.printList(prev)
                
            prev = prev.next
                
        return dummy.next
        
    def printList(self, L):
        Ls = []
        while L:
            Ls.append("{}".format(L.val))
            L = L.next
            
            
        print(" ->".join(Ls))
            
