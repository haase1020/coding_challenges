# Problem from CodeSignal Challenge
# prompt: given the root of a binary tree where each node contains
# an integer, determine the sum of all the integer values
# in the tree.

# following code provided: binary trees are already defined with this interface:
class Tree(object):
    def __init__(self,  x):
        self.value = x
        self.left = None
        self.right = None

# this is the code I added:


def tree_paths_sum(root):
    if(root == None):
        return 0
    return (root.value + tree_paths_sum(root.left) + tree_paths_sum(root.right))
