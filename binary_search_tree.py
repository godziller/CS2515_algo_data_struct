from PIL.ImImagePlugin import number


class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.sum = 0

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            #add data into left subtree
            if self.left:
                self.left.add_child(data)                   #recursivly call add_child
            else:                                           # if no tree exists
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)                  #recursivly call add_child
            else:                                           # if no tree exists
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit the base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val<self.data:
            #val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False            #value doesnt exist in tree

        if val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False  # value doesnt exist in tree

    def find_min(self):
        #visit left tree
        if self.left:                       # if left tree exists
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        #visit right tree
        if self.right:
            return self.right.find_max()
        else:
            return self.data



    def delete(self, val):
        if val < self.data:         # if val is in the left subtree
            if self.left:           # if we have something in the left subtree
                self.left = self.left.delete(val)       #set this to check ITS left tree for the value
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val) 



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34,18,4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(200))
    print(numbers_tree.find_min())