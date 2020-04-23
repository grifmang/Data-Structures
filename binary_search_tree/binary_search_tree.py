import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # recursive `insert` implementation
    # does not return anything when executed
    # THIS WILL NOT WORK :) 
    #   def insert(self, value):
    #     # base case: we found a parking spot!
    #     # we're in an empty spot in the tree 
    #     if self is None:
    #         self = BinarySearchTreeNode(value)
    #     # if we aren't at the base case, move towards it 
    #     else:
    #         # self is a node with a value 
    #         # compare the value to the value at this node 
    #         if value < self.value:
    #             # move to the left
    #             self.left.insert(value)
    #         # otherwise, value >= self.value
    #         else:
    #             self.right.insert(value)

    def insert(self, value):
        # self.left and/or self.right need to be valid nodes 
        # for us to call `insert` on them 
        if value < self.value:
            # check if self.left is a valid node 
            if self.left:
                self.left.insert(value)
            # the left side is empty 
            else:
                # we've found a valid parking spot 
                self.left = BinarySearchTree(value)
        # otherwise, value >= self.value
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        while True:
            cb(self.value)
            while(self.right):
                return cb(self.value)
            while(self.left):
                return cb(self.value)
            break

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
