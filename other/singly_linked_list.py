# this was in question in challenge
class ListNode(object):
    def __init__(self):
        self.value = None
        self.next = None

# the linked list class was not listed in the challenge prompt

# my addition

# time and space complexity is 0(n)


def condense_linked_list(node):
    current = node
    no_dupes = []
    while current is not None:
        if current.value not in no_dupes:
            no_dupes.append(current.value)
        current = current.next
    return no_dupes


test_list = ListNode()
print(test_list.value)
