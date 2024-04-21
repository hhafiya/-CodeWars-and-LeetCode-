# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val, self.left, self.right}'
class Solution:
    def search_node(self, root, key):
        found = False
        current = root
        found_node = None
        parent = None
        while not found:
            if current.val > key and current.left:
                parent = current
                current = current.left
            elif current.val < key and current.right:
                parent = current
                current = current.right
            elif current.val == key:
                found = True
                found_node = current
            else:
                break
        if not found:
            return None, None
        return found_node, parent

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def deleteNode(self, root, key):
        if not root:
            return root
        node_to_delete, parent = self.search_node(root, key)
        if not node_to_delete:
            return root

        if node_to_delete.left and node_to_delete.right:
            successor = self.find_min(node_to_delete.right)
            node_to_delete.val = successor.val
            node_to_delete.right = self.deleteNode(node_to_delete.right, successor.val)
        else:
            if not node_to_delete.left:
                child = node_to_delete.right
            else:
                child = node_to_delete.left
            if not parent:
                root = child
            elif parent.left == node_to_delete:
                parent.left = child
            else:
                parent.right = child
        return root
