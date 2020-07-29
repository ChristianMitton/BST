class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, number):        
        self.root = self.addHelper(self.root, number)

    def addHelper(self, root, number):
        if root == None:            
            return BSTNode(number)
        
        if number < root.val:
            root.left = self.addHelper(root.left, number)
        
        elif number >= root.val:
            root.right = self.addHelper(root.right, number)
        
        return root
        
    def delete(self, target):
        self.root = self.deleteHelper(self.root, target)
    
    def deleteHelper(self, root, target):
        if root == None:
            return None
        
        if target < root.val:
            root.left = self.deleteHelper(root.left, target)
        elif target > root.val:
            root.right = self.deleteHelper(root.right, target)
        else:
            # case1 no children:
            if root.left == None and root.right == None:
                return None
            # case2 1 child:
            if root.left != None and root.right == None:
                return root.left
            if root.right != None and root.left == None:
                return root.right                
            # case3 2 children:
            # go left once, then all the way right            
            inorderSuccessor = None
            ptr = root.right
            while ptr != None:
                inorderSuccessor = ptr
                ptr = ptr.left
            # replace root with inorder successor's val
            root.val = inorderSuccessor.val
            # call deleteHelper on current root node to delete extra inorder successor            
            root.right = self.deleteHelper(root.right, inorderSuccessor.val)
        
        return root
        

    def inorder(self):
        self.inorderHelper(self.root)
    
    def inorderHelper(self, root):
        if root == None:
            return
        
        self.inorderHelper(root.left)
        print(root.val)
        self.inorderHelper(root.right)    


bst = BST()
bst.add(10)
# left branch
bst.add(5)
bst.add(2)
bst.add(1)
bst.add(5)
# right branch
bst.add(15)
bst.add(13)
bst.add(12)
bst.add(14)
bst.add(22)
# ----------------
# bst.inorder()
# bst.delete(10)
# bst.inorder()