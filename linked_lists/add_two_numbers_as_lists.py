# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        
        carr = 0
        
        headA = A
        headB = B
        
        head = ListNode(0)
        currHead = head
        
        while headA and headB:
            print(headA.val, headB.val)
            sm = headA.val + headB.val + carr
            
            if sm > 9:
                sm = sm % 10
                carr = 1
                
            else:
                carr = 0
                
                
            newNode = ListNode(sm)
            currHead.next = newNode
            currHead = newNode
            
            headA = headA.next
            headB = headB.next
            
        while headA:
            sm = headA.val + carr
            if sm > 9:
                sm = sm % 10
                carr = 1
            else:
                carr = 0
                
            newNode = ListNode(sm)
            currHead.next = newNode
            currHead = newNode
            
            headA = headA.next
            
        while headB:
            sm = headB.val + carr
            if sm > 9:
                sm = sm % 10
                carr = 1
            else:
                carr = 0
                
            newNode = ListNode(sm)
            currHead.next = newNode
            currHead = newNode
            
            headB = headB.next
            
        if carr > 0:
            newNode = ListNode(carr)
            currHead.next = newNode
            
                
            
        return head.next
