# # this was in question in challenge
# class ListNode(object):
#     def __init__(self, x):
#         self.value = x
#         self.next = None

# # the linked list class was not listed in the challenge prompt


# class LinkedList:
#     # initialize head
#     def __init__(self):
#         self.head = None
#     # function to insert a new node at the beginning

#     def push(self, new_data):
#         new_node = ListNode(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def deleteNode(self, key):
#         temp = self.head
#         if (temp is not None):
#             if (temp.value == key):
#                 self.head = temp.next
#                 temp = None
#                 return
#         while(temp is not None):
#             if temp.value == key:
#                 break
#             prev = temp
#             temp = temp.next

#         # if key was not present in
#         # linked list
#         if(temp == None):
#             return

#         # Unlink the node from linked list
#         prev.next = temp.next

#         temp = None

#     # Utility function to print the
#     # linked LinkedList
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print(temp.value, end=' ')
#             temp = temp.next

#     def remove_dups(node):
#         current = node
#         if current is None:
#             return
#         no_dupes = []
#         while current is not None:
#             if current.value not in no_dupes:
#                 no_dupes.append(current.value)
#             current = current.next
#         return no_dupes

# current = ll.head
# while current:
#     runner = current
#     while runner.next:
#         if runner.next.value == current.value:
#             runner.next = runner.next.next
#         else:
#             runner = runner.next
#     current = current.next
# return ll.head


llist = LinkedList()

llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
      "duplicate elements:")
llistt.remove_dups()
llist.printList()
