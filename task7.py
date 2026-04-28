class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def check(l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False

        return (l.val == r.val and
                check(l.left, r.right) and
                check(l.right, r.left))

    return check(root.left, root.right)