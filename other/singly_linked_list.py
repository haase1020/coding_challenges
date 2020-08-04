from random import randint


class LinkedListNode:

    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    # def generate(self, n, min_value, max_value):
    #     self.head = self.tail = None
    #     for i in range(n):
    #         self.add(randint(min_value, max_value))
    #     return self


def remove_dups(ll):
    current = ll
    if current is None:
        return
    no_dupes = []
    while current is not None:
        if current.value not in no_dupes:
            no_dupes.append(current.value)
        current = current.next
    return no_dupes

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


ll = LinkedList([1, 5, 4, 7, 7, 6, 5, 5, 5, 9, 10])
# ll.generate(100, 0, 9)
print("linked list", ll)
remove_dups(ll)
print("dupes removed", ll)