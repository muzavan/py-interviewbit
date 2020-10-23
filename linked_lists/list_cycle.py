# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        head = A
        A1 = A
        A2 = A
        
        while A2 and A2.next:
            A1 = A1.next
            A2 = A2.next.next
            
            if A1 == A2:
                break
            
        if not A2 or not A2.next:
            return None
            
        A1 = head
        while A1 != A2:
            A1 = A1.next
            A2 = A2.next
            
        return A1
