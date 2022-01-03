#!/usr/bin/python3.10

class BinarySearchTreeNode:
    def __init__(self, data=None):
        self.root = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        # set main root 
        if self.root is None:
            self.root = data
    
        if self.root == data:
            return

        if data < self.root:
            # add to left subtree
            if self.left is None:
                self.left = BinarySearchTreeNode(data)
            else:
                self.left.insert(data)
        else: 
            # add right subtree
            if self.right is None:
                self.right = BinarySearchTreeNode(data)
            else:
                self.right.insert(data)
   
    def search(self, data):
        # print(f"root:{self.root} vs data:{data}")
        if self.root == data:
            return True
        
        if data < self.root:
            if self.left is not None:
                return self.left.search(data)
            else:
                return False
        
        if data > self.root:
            if self.right is not None:
                return self.right.search(data)
            else:
                return False
        
    def max(self):
        if self.right is None:
            return self.root
    
        return self.right.max()

    def min(self):
        if self.left is None:
            return self.root

        return self.left.min()      

    def in_order_traversal(self):
        elements = []
        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit root
        elements.append(self.root)

        #vist right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements

    def delete(self, data):
        if data < self.root:
            if self.left is None:
                return
            self.left = self.left.delete(data)
        
        elif data > self.root:
            if self.right is None:
                return 
            self.right = self.right.delete(data)
        else:
            # if both childs are None
            if self.right is None and self.left is None:
                return None
            # if left is None
            if self.left is None:
                return self.right
            # if right is None
            elif self.right is None:
                return self.left

            # Both childs exists
            min_value = self.right.min()
            self.root = min_value
            self.right = self.right.delete(min_value)
        
        return self 
        
if __name__ == '__main__':

    numbers = [6, 15, 4, 5, 9, 16]
    bst = BinarySearchTreeNode()
    print(f"inserting:",end=" ")
    for item in numbers:
        print(f"{item}",end=" ")
        bst.insert(item)
    print()

    print(f"inorder traversal:{bst.in_order_traversal()}")
    num_to_del = 6
    bst.delete(num_to_del)
    print(f"after deleting {num_to_del}: {bst.in_order_traversal()}")

    for i in [-1, 100, 6, 5]:
        print(f"is {i} in BST ? {bst.search(i)}")

    print(f"max value: {bst.max()}")
    print(f"min value: {bst.min()}")
        
    
