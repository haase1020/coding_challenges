# write a function that takes in a potentially invalid BST and returns a boolean representing whether the BST is valid
# assuming strict BST


# time complexity 0(n)(traversing every node in tree) | space complexity 0(d) (depth of tree)/ 0(n) if 1 branch
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


# passes tests in AlgoExpert
