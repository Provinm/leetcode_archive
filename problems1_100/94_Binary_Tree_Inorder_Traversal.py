'''

94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.res = []
        if not root:
            return self.res
        self.inorder(root)
        return self.res

    def inorder(self, root):

        if root.left:
            self.inorder(root.left)
        
        if root.val:
            self.res.append(root.val)

        if root.right:
            self.inorder(root.right)
                

