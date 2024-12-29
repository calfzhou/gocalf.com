from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional['ListNode'], root: Optional['TreeNode']) -> bool:
        def match(head: 'ListNode', root: 'TreeNode') -> bool:
            if head is None: return True
            if root is None or root.val != head.val: return False
            return match(head.next, root.left) or match(head.next, root.right)

        stack = []
        while root or stack:
            if root:
                if match(head, root): return True
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right

        return False
