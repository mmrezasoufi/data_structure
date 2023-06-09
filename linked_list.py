class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._head is None

    def first(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self._head.val

    def last(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self._tail.val

    def add_first(self, value):
        newest = Node(value)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest.next = self._head
            self._head = newest

    def add_last(self, value):
        newest = Node(value)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            self._tail.next = newest
            self._tail = newest
            newest.next = None

    def remove_first(self):
        if self.is_empty():
            raise Exception("Empty list")

        # This means that the list contains one element
        if self._head.next is None:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next

    def remove_last(self):
        if self.is_empty():
            raise Exception("Empty list")

        if self._head.next is None:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.next.next is not None:
                current = current.next
            current.next = None

    def search(self, value):
        current = self._head
        while current is not None:
            if current.val == value:
                return current
            current = current.next
        return False

    def traversal(self):
        if self.is_empty():
            print("Linked List is empty.")
            return
        current = self._head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.add_first(10)
linked_list.add_last(20)
linked_list.add_first(30)
linked_list.add_last(5)
linked_list.traversal()
linked_list.remove_last()
linked_list.traversal()
linked_list.remove_first()
linked_list.traversal()
