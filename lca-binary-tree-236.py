# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (p, q, None): return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left == None:
            return right
        elif right == None:
            return left
        else:
            return root

# The Idea is that we pass the node recursively and wait till it
# returns the Target Node, if the target is not found then we 
# recursively pass None each time untill it reaches the root. 
# So if left or right returns None then the other target will 
# definitely be present in the other node only so its no use 
# checking the level it is present. Also since in LCA a node 
# can be a descendent of itself it can stop with the first hit 
# in a branch if the other branch returns a None. If both the 
# branches dont return None then we return the root as LCA