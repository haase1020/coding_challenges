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
# using recursion where base case is root == None return 0
# time complexity: 0(n) where n are the number of the nodes in the binary tree


def tree_paths_sum(root):
    if(root == None):
        return 0
    return (root.value + tree_paths_sum(root.left) + tree_paths_sum(root.right))


# to test code:
if __name__ == '__main__':
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.left = Tree(6)
    root.right.right = Tree(7)
    root.right.left.right = Tree(8)

    sum = tree_paths_sum(root)

    print("Sum of all the nodes is:", sum)
