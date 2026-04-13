class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate_bst(top):    
    def check_subtree(node, max_lim=None, min_lim=None):        
        if not node: return True
        
        if (max_lim is not None and node.val >= max_lim) or (min_lim is not None and node.val <= min_lim):
            return False
        
        return check_subtree(node.left, max_lim=node.val, min_lim=min_lim) and check_subtree(node.right, max_lim=max_lim, min_lim=node.val)
    
    return check_subtree(top)


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(validate_bst(root1))


root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(validate_bst(root2))


root3 = TreeNode(1)

print(validate_bst(root3))


root4 = None

print(validate_bst(root4))


root5 = TreeNode(10)
root5.left = TreeNode(5)
root5.right = TreeNode(15)
root5.right.left = TreeNode(6)
root5.right.right = TreeNode(20)

print(validate_bst(root5))


root6 = TreeNode(8)
root6.left = TreeNode(3)
root6.right = TreeNode(10)
root6.left.left = TreeNode(1)
root6.left.right = TreeNode(6)
root6.left.right.left = TreeNode(4)
root6.left.right.right = TreeNode(7)
root6.right.right = TreeNode(14)
root6.right.right.left = TreeNode(13)

print(validate_bst(root6))


root7 = TreeNode(2)
root7.left = TreeNode(2)
root7.right = TreeNode(3)

print(validate_bst(root7))


root8 = TreeNode(10)
root8.left = TreeNode(5)
root8.right = TreeNode(15)
root8.left.right = TreeNode(12)

print(validate_bst(root8))