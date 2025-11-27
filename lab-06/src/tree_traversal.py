from collections import deque

def inorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_recursive(node.left, result)
        result.append(node.value)
        inorder_recursive(node.right, result)
    return result

def preorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        preorder_recursive(node.left, result)
        preorder_recursive(node.right, result)
    return result

def postorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        postorder_recursive(node.left, result)
        postorder_recursive(node.right, result)
        result.append(node.value)
    return result

def inorder_iterative(root):
    """Итеративный in-order обход с использованием стека. O(n)"""
    stack, result = [], []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result