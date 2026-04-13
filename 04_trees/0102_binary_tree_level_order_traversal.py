from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_level_order_traversal(top):
    if not top: return []
    node_queue = deque()
    node_queue.append(top)
    result = []
    
    while node_queue:
        level = []
        level_size = len(node_queue)
        for _ in range(level_size):
            node = node_queue.popleft()
            level.append(node.val)
            if node.left: node_queue.append(node.left)
            if node.right: node_queue.append(node.right)
        result.append(level)
    
    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(bfs_level_order_traversal(root))


root = TreeNode(1)

print(bfs_level_order_traversal(root))


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

print(bfs_level_order_traversal(root))


root = None

print(bfs_level_order_traversal(root))