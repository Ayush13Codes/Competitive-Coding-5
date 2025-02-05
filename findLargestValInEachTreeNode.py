# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            maxInLvl = q[0].val
            for _ in range(len(q)):
                node = q.popleft()
                maxInLvl = max(maxInLvl, node.val)
                # Check if the node has valid children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxInLvl)

        return res
        # T: O(n), S: O(n)
