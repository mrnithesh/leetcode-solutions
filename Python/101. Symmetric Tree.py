# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        
        def isMirror(t1,t2):
            if (t1==None and t2==None):
                return True
            elif (t1==None or t2==None):
                return False
            else:
                return (t1.val == t2.val) and isMirror(t1.left,t2.right) and isMirror(t1.right,t2.left)
        return isMirror(root.left,root.right)