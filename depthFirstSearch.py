# you are given a Node class that has a name and an array of optional children nodes.
# When put together, nodes form an acyclic tree like structure.
# implement the depthFirstSearch method on the Node class, which takes in an empyty array,
# traverses the tree using DFS, stores all of the node's names in the input array, and returns it.

# Time complexity is 0(V + E)
# Space complexity is 0(V)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
