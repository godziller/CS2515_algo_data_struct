
class BinaryTreeNode(object):
    def __init__(self, element, leftchild, rightchild):
        self._element = element
        self._rightchild = rightchild
        self._leftchild = leftchild

    def get_element(self):
        return self._element

    def get_rightchild(self):
        return self._rightchild

    def get_leftchild(self):
        return self._leftchild

    def set_rightchild(self, node):
        self._rightchild = node

    def set_leftchild(self, node):
        self._leftchild = node


class BinaryTree(object):
    def __init__(self):
