class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, [], [])

    def traverse(self, root: Optional[TreeNode], gt: List[int], lt: List[int]) -> bool:
        left = True
        right = True
        for item in lt:
            if root.val >= item:
                return False
        for item in gt:
            if root.val <= item:
                return False

        if root.left != None:
            left = self.traverse(root.left, gt, lt + [root.val])
        if root.right != None:
            right = self.traverse(root.right, gt + [root.val], lt)
        return left and right
