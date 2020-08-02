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


print(nodeDepths(
    {
        "nodes": [
            {"children": ["B"], "id": "A", "value": "A"},
            {"children": ["C"], "id": "B", "value": "B"},
            {"children": ["D", "E"], "id": "C", "value": "C"},
            {"children": ["F"], "id": "D", "value": "D"},
            {"children": [], "id": "E", "value": "E"},
            {"children": [], "id": "F", "value": "F"}
        ],
        "startNode": "A"
    }
)
)
