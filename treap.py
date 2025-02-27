class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def insert(self, root, key, priority):
        if root is None:
            return Node(key, priority)
        if key < root.key:
            root.left = self.insert(root.left, key, priority)
            if root.left.priority > root.priority:
                root = self.rotate_right(root)
        else:
            root.right = self.insert(root.right, key, priority)
            if root.right.priority > root.priority:
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
            if root.left.priority < root.right.priority:
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
