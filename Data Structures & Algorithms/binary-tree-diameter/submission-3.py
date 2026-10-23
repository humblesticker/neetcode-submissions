class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode]) -> tuple(int, int):
            if node is None: return (-1, -1)

            lp, lb = traverse(node.left)
            rp, rb = traverse(node.right)

            path = lb + rb + 2
            max_path = max(path, lp, rp)
            max_branch = max(lb, rb) + 1
            return max_path, max_branch

        return traverse(root)[0] 

"""
# return (path, branch)
def traverse(node: Optional[TreeNode]) -> tuple(int, int):
    if node is None: return (-1, -1)
    lpath, lbranch = traverse(node.left)
    rpath, rbranch = traverse(node.right)
    path = lbranch + rbranch + 2
    max_path = max(path, lpath, rpath)
    max_branch = max(lbranch, rbranch) + 1
    return (max_path, max_branch)

return traverse(root)[0] 

test
  1
    3
   2   4
  5      7
node, return
5, (0,0)
2, (1,1)
7, (0,0)
4, (1,1)
3, (4,2)
1, (4,3)

[1,2,3]
node, return
2, (0,0)
3, (0,0)
1, (2,1)

1: 0 ok


The path does not necessarily have to pass through the root.
is this possible? yes 
  1
    3
   2   4
  5      7

post_order
node, return (path, branch)
5, (0,0) - (-1,-1) return for None
2, (1,1)
7, (0,0)
4, (1,1)
3, (4,2)
1, (4,4)
return 4

at node 2 actions
- max branch, 1+ld or 1+rd (to be used by parent): dict(node, val)
- update max_path = max(max_path, ld+rd+2)

leaf node d = 0
None is -1
"""