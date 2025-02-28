class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None

class Treap:
    def __init__(self):
        self.root = None

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right:
            new_root.right.parent = node
        new_root.right = node
        new_root.parent = node.parent
        node.parent = new_root
        if new_root.parent is None:
            self.root = new_root
        elif new_root.parent.left == node:
            new_root.parent.left = new_root
        else:
            new_root.parent.right = new_root
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left:
            new_root.left.parent = node
        new_root.left = node
        new_root.parent = node.parent
        node.parent = new_root
        if new_root.parent is None:
            self.root = new_root
        elif new_root.parent.left == node:
            new_root.parent.left = new_root
        else:
            new_root.parent.right = new_root
        return new_root

    def insert(self, root, key, priority):
        if root is None:
            return Node(key, priority)
        if key < root.key:
            root.left = self.insert(root.left, key, priority)
            root.left.parent = root
            if root.left.priority < root.priority:  # Change to maintain min-heap property
                root = self.rotate_right(root)
        else:
            root.right = self.insert(root.right, key, priority)
            root.right.parent = root
            if root.right.priority < root.priority:  # Change to maintain min-heap property
                root = self.rotate_left(root)
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            if root.left.priority > root.right.priority:  # Change to maintain min-heap property
                root = self.rotate_left(root)
                root.left = self.delete(root.left, key)
            else:
                root = self.rotate_right(root)
                root.right = self.delete(root.right, key)
        return root

    def insert_key(self, key, priority):
        self.root = self.insert(self.root, key, priority)

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"Key: {root.key}, Priority: {root.priority}")
            self.inorder(root.right)

    def print_treap(self):
        self.inorder(self.root)
