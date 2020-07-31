# Problem from CodeSignal Challenge

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    current = node
    list = []
    while current is not None:
        if current.value not in list:
            list.append(current.value)
            current = current.next

    return list
