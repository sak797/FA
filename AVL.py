# https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

class Node():
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree():

    def insert(self, root, val):
        if not root:
            return Node(val)
        elif root.value < val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and val < root.left.value:
            return self.rightRotate(root)
        if balance < -1 and val > root.right.value:
            return self.leftRotate(root)
        if balance > 1 and val > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, root):
        y = root.right
        T1 = y.left
        y.left = root
        root.right = T1
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, root):
        y = root.left
        T3 = y.right
        y.right = root
        root.left = T3
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(str(root.value) + " --> ", end = "")
            self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return
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

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minVal(root.right)
            root.val = temp.value
            root.right = self.delete(root.right, temp.value)
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

if __name__ == '__main__':
    t = AVL_Tree()
    root = None
    insert_list = [4, 7, 2, 6, 5, 8]
    for val in insert_list:
        root = t.insert(root, val)

    t.preorder(root)
    print("")
    root = t.delete(root, 7)
    root = t.delete(root, 8)
    t.preorder(root)
    print("")

