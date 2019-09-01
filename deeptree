class TreeNode():
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None
class Solution():
   def deeptree(self, Root):
      if Root is None:
         return 0
      left = self.deeptree(Root.left)
      right = self.deeptree(Root.right)
      return max(left, right)+1

c = TreeNode(2)
d = TreeNode(4)
e = TreeNode(7)
c.left = d
d.right = e

a = Solution()
b = a.deeptree(c)
print(b)
