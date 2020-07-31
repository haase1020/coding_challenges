# prompt: the distance between a node in a binary tree and the tree's root is called the node's depth.
# write a function that takes in a binary tree and returns the sume of it's node depths

# time complexity: 0(n) space complexity for recursive and iterative: 0(h) where h is height
# # iterative approach:
# def nodeDepths(root):
#     sumOfDepths = 0
#     stack = [{"node": root, "depth": 0}]
#     while len(stack) > 0:
#         nodeInfo = stack.pop()
#         node, depth = nodeInfo["node"], nodeInfo["depth"]
#         if node is None:
#             continue
#         sumOfDepths += depth
#         stack.append({"node"" node.left, "depth": depth + 1})
#         stack.append({"node"" node.right, "depth": depth + 1})

# recursive approach:
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    # handle base case of recursion
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


print(BinaryTree({
    "tree": {
        "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "2", "left": "4", "right": "5", "value": 2},
            {"id": "3", "left": "6", "right": "7", "value": 3},
            {"id": "4", "left": "8", "right": "9", "value": 4},
            {"id": "5", "left": null, "right": null, "value": 5},
            {"id": "6", "left": null, "right": null, "value": 6},
            {"id": "7", "left": null, "right": null, "value": 7},
            {"id": "8", "left": null, "right": null, "value": 8},
            {"id": "9", "left": null, "right": null, "value": 9}
        ],
        "root": "1"
    }
}))
