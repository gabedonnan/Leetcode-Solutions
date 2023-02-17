# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root_node: Optional[TreeNode]) -> int:

        def search(root: Optional[TreeNode], prevs: List[int]) -> int:
            if len(prevs) > 0:
                prevdiff = min([abs(root.val - prev) for prev in prevs])
            else:
                prevdiff = math.inf
            #print(root.val, prevs, prevdiff)
            if root.left == None and root.right == None:
                return prevdiff
            elif root.left == None and root.right != None:
                return min([abs(root.val - root.right.val), search(root.right, prevs + [root.val]), prevdiff])
            elif root.right == None and root.left != None:
                return min([abs(root.val - root.left.val), search(root.left, prevs + [root.val]), prevdiff])
            else:
                return min([search(root.left, prevs + [root.val]), search(root.right, prevs + [root.val]), abs(root.val - root.left.val), abs(root.val - root.right.val), prevdiff])
        return search(root_node, [])
            
