# find the closest value in binary search tree
# avg time = 0(log(n)) | worst case = 0(n), which is tree with 1 branch
# space complexity: if recursively, avg. and worst are same as time. Iteratively: 0(1) both avg and worst case


# recursive method:
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest

# iterative method:


# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, tree.value)


# def findClosestValueInBstHelper(tree, target, closest):
#     currentNode = tree
#     while currentNode is not None:
#         if abs(target - closest) > abs(target - currentNode.value):
#             closest = currentNode.value
#         if target < currentNode.value:
#             currentNode = currentNode.left
#         elif target > currentNode.value:
#             currentNode = currentNode.right
#         else:
#             break
#     return closest


# # this is the class of the input tree. Do not edit:
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
