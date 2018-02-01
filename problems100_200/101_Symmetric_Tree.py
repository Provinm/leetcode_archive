'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        vals = []
        tree = [root]
        idx = 0
        scale = 1
        tem_scale = 0
        for br in tree:
            
            if br:
                vals.append(br.val)
                l = br.left
                r = br.right
                if l and r:
                    tem_scale += 2
                elif not l and not r:
                    pass
                else:
                    tem_scale += 1
                scale -= 1  
            else:
                vals.append(None)
            
            if len(vals) == pow(2, idx):
                if len(vals) == 1:
                    vals = []
                else:
                    while vals:
                        f = vals.pop(0)
                        l = vals.pop(-1)
                        if f == l:
                            pass
                        else:
                            return False

                idx += 1

        return True

    


            



            
            