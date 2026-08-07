# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0
        def canReachNode(root, sum, target):
            if not root:
                return False
            sum += root.val

            if not root.left and not root.right and sum == target:
                return True
            if canReachNode(root.left, sum, target):
                return True
            if canReachNode(root.right, sum, target):
                return True
            
            sum -= root.val
            return False
        
        return canReachNode(root, sum, targetSum)