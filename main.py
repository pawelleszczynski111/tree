from typing import Any


class BinaryNode:
    def __init__(self, value:Any):
        self.value = value
        self.left_child: BinaryNode = None
        self.right_child: BinaryNode = None
        self.parent: BinaryNode = None

    def __str__(self):
        return str(self.value)

    def level_of(self):
        lvl = 0
        parent = self.parent
        while parent != None:
            lvl += 1
            parent = parent.parent

        return lvl


    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        return True

    def add_left_child(self, value:Any):
        self.left_child = BinaryNode(value)
        self.left_child.parent = self

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)
        self.right_child.parent = self

    def traverse_in_order(self):

        if self.left_child:
            type(self).traverse_in_order(self.left_child)
        print(self.value)
        if self.right_child:
            type(self).traverse_in_order(self.right_child)

    def traverse_post_order(self):
        if self.left_child:
            type(self).traverse_post_order(self.left_child)
        if self.right_child:
            type(self).traverse_post_order(self.right_child)
        print(self.value)

    def traverse_pre_order(self):
        print(self.value)
        if self.left_child:
            type(self).traverse_pre_order(self.left_child)
        if self.right_child:
            type(self).traverse_pre_order(self.right_child)

class BinaryTree:
    def __init__(self, root: BinaryNode):
        self.root = root

    def traverse_in_order(self):
        if type(self) is BinaryTree:
            if self.root.left_child:
                BinaryTree.traverse_in_order(self.root.left_child)
            print(self.root.value)
            if self.root.right_child:
                BinaryTree.traverse_in_order(self.root.right_child)
        if type(self) is BinaryNode:
            if self.left_child:
                BinaryTree.traverse_in_order(self.left_child)
            print(self.value)
            if self.right_child:
                BinaryTree.traverse_in_order(self.right_child)

    def traverse_post_order(self):
        if type(self) is BinaryTree:
            if self.root.left_child:
                BinaryTree.traverse_post_order(self.root.left_child)

            if self.root.right_child:
                BinaryTree.traverse_post_order(self.root.right_child)
            print(self.root.value)
        if type(self) is BinaryNode:
            if self.left_child:
                BinaryTree.traverse_post_order(self.left_child)

            if self.right_child:
                BinaryTree.traverse_post_order(self.right_child)
            print(self.value)

    def traverse_pre_order(self):
        if type(self) is BinaryTree:
            print(self.root.value)
            if self.root.left_child:
                BinaryTree.traverse_pre_order(self.root.left_child)

            if self.root.right_child:
                BinaryTree.traverse_pre_order(self.root.right_child)

        if type(self) is BinaryNode:
            print(self.value)
            if self.left_child:
                BinaryTree.traverse_pre_order(self.left_child)

            if self.right_child:
                BinaryTree.traverse_pre_order(self.right_child)



    def show(self):
        spacer = " |===|"
        if type(self) is BinaryTree:
            if self.root.right_child:
                BinaryTree.show(self.root.right_child)
            print("|"+str(self.root.value)+"|")
            if self.root.left_child:
                BinaryTree.show(self.root.left_child)
        if type(self) is BinaryNode:
            if self.right_child:
                BinaryTree.show(self.right_child)

            print("  " + spacer*self.level_of()+str(self.value)+"|")
            if self.left_child:
                BinaryTree.show(self.left_child)





bn = BinaryNode(10)

bn.add_left_child(9)
bn.add_right_child(2)

bn.left_child.add_left_child(1)
bn.left_child.add_right_child(3)

bn.right_child.add_left_child(4)
bn.right_child.add_right_child(6)

bn.left_child.left_child.add_left_child(5)
bn.left_child.right_child.add_right_child(7)

bn.right_child.left_child.add_right_child(8)
bn.right_child.right_child.add_left_child(0)


# bn.traverse_pre_order()
bt = BinaryTree(bn)
# bt.traverse_pre_order()
bt.show()