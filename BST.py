# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

class Node():
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

class BST():
    def __init__(self, key):
        self.root = Node(key)

    def insert(self, root, val):
        if root:
            if root.value < val:
                if root.right is None:
                    root.right = Node(val)
                else:
                    self.insert(root.right, val)
            else:
                if root.left is None:
                    root.left = Node(val)
                else:
                    self.insert(root.left, val)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(str(root.value) + " --> ", end = "")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(str(root.value) + " --> ", end="")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.value) + " --> ", end="")

    def search(self, root, val):
        if root:
            if root.value == val:
                return root
            elif root.value < val:
                return self.search(root.right, val)
            elif root.value > val:
                return self.search(root.left, val)
        else:
            return root

    def minVal(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(self, root, key):
        if root is None:
            return root
        if root.value > key:
            root.left = self.deleteNode(root.left, key)
        elif root.value < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.minVal(root.right)
                root.value = successor.value
                root.right = self.deleteNode(root.right, successor.value)
        return root

if __name__ == '__main__':
    t = BST(5)
    insert_list = [4, 7, 2, 6, 3, 8]
    for val in insert_list:
        t.insert(t.root, val)

    t.inorder(t.root)
    print("")
    t.preorder(t.root)
    print("")
    t.postorder(t.root)
    print("")
    print(t.search(t.root, 4).left.value)
    print(t.search(t.root, 1))
    print(t.minVal(t.root.right).value)
    root =  t.deleteNode(t.root, 8)
    t.inorder(root)
    print("")