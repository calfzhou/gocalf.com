from utils import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        parts = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                parts.append(str(root.val))
                root = root.left
            else:
                parts.append('')
                root = stack.pop().right

        return ','.join(parts)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = [TreeNode(int(s)) if s else None for s in data.split(',')]
        virtual = TreeNode(None)
        stack = [virtual]
        root = None
        for node in nodes:
            if root:
                stack.append(root)
                root.left = root = node
            else:
                stack.pop().right = root = node

        return virtual.right


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
