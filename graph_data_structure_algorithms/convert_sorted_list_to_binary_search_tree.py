# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        return convert(A)
    
def convert(A):
    if A is None:
        return None
    
    ln = 0
    head = A
    while head:
        ln += 1
        head = head.next
        
    mid = ln // 2
    
    idx = 0
    head = A
    prev = None
    while idx < mid:
        prev = head
        head = head.next
        idx += 1
        
    tr = TreeNode(head.val)
    
    if prev is not None:
        prev.next = None
        tr.left = convert(A)
        
    nxt = head.next
    if nxt is not None:
        tr.right = convert(nxt)
        
    return tr



