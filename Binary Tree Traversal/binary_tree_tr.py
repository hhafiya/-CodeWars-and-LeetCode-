from collections import deque
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node):
    result = []
    stack = deque([node])
    if not node:
        return []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

# In-order traversal
def in_order(node):
    result = []
    stack = []
    current = node

    while stack or current:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.data)
            current = current.right

    return result

# Post-order traversal
def post_order(node):
    result = []
    stack = deque([node])
    if not node:
        return []

    while stack:
        current = stack.pop()
        result.append(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return result[::-1]
