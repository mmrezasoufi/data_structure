# Stack implementation using linked list

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        newest = Node(value)
        newest.next = self._head
        self._head = newest
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack")
        answer = self._head.val
        self._head = self._head.next
        self._size -= 1
        return answer

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


stack = LinkedStack()
stack.push(2)
stack.push(22)
stack.push(21)
stack.push(12)
stack.push(29)
stack.push(14)
stack.push(17)
print(stack.search(12).val)
stack.push(9)
stack.pop()
stack.traversal()
