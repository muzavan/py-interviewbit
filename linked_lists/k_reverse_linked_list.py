# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        head = A
        tempHead = A
        
        nA = 0
        while tempHead:
            nA += 1
            tempHead = tempHead.next
            
        if nA <= 1 or B == 1:
            return A
            
        tempHead = A
        times = nA//B
        prevTail =  None
        
        for _ in range(times):
            n = 1
            start = tempHead
            
            while n < B:
                n += 1
                tempHead = tempHead.next
                
            tmp = tempHead
            tempHead = tempHead.next
            tmp.next = None
            
            newHead, newTail = self.reverseAllList(start)
            
            newTail.next = tempHead
            if prevTail:
                prevTail.next = newHead
                
            prevTail = newTail
                
            if _ == 0:
                head = newHead
                
        return head
    
    
    def reverseAllList(self, A):
        # self.printList(A)
        newTail = A
        prev = None
        while A:
            tmp = A.next
            A.next = prev
            prev = A
            A = tmp
            
        return prev, newTail
        
    def printList(self, A):
        As = []
        while A:
            As.append("{}".format(A.val))
            A = A.next
            
        print(" -> ".join(As))
            
        
            
            
        
